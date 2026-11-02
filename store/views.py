from decimal import Decimal
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Product
from .translations import get_language, get_texts


def localize_product(product, language):
    product.display_name = product.localized_name(language)
    product.display_description = product.localized_description(language)
    return product


def safe_next_url(request, fallback="product_list"):
    next_url = request.POST.get("next", "") or request.GET.get("next", "")
    if next_url.startswith("/") and not next_url.startswith("//"):
        return next_url
    return reverse(fallback)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    localize_product(product, get_language(request))
    return render(
        request,
        "store/product_detail.html",
        {
            "product": product,
            "is_saved": product.id in request.session.get("saved", []),
        },
    )


def product_list(request):
    language = get_language(request)
    products = Product.objects.all()

    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "")
    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")
    in_stock = request.GET.get("in_stock", "")
    sort = request.GET.get("sort", "featured")

    # Search
    if query:
        products = products.filter(
            Q(name_en__icontains=query) |
            Q(name_hy__icontains=query) |
            Q(name_ru__icontains=query)
        )

    # Filters
    if category:
        products = products.filter(category=category)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    if in_stock == "1":
        products = products.filter(stock__gt=0)

    # Sorting
    if sort == "price_low":
        products = products.order_by("price")
    elif sort == "price_high":
        products = products.order_by("-price")
    elif sort == "name":
        products = products.order_by(f"name_{language}")
    else:
        products = products.order_by("-is_featured")

    products = [localize_product(product, language) for product in products]

    return render(
        request,
        "store/product_list.html",
        {
            "products": products,
            "filters": request.GET,  # Ուղղվել է request.Get -> request.GET
            "saved_ids": request.session.get("saved", []),
        },
    )


def set_language(request, language):
    if language in {"en", "hy", "ru"}:
        request.session["lang"] = language
    next_url = request.GET.get("next", "/")
    if not next_url.startswith("/") or next_url.startswith("//"):
        next_url = "/"
    return redirect(next_url)


def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not product.in_stock:
        return HttpResponseBadRequest("Product is out of stock")
    basket = request.session.get("basket", {})
    key = str(product.id)
    basket[key] = min(int(basket.get(key, 0)) + 1, product.stock)
    request.session["basket"] = basket

    saved = request.session.get("saved", [])
    if product.id in saved:
        saved.remove(product.id)
        request.session["saved"] = saved

    messages.success(request, get_texts(request)["added"])
    return redirect(safe_next_url(request))


def basket_view(request):
    language = get_language(request)
    basket = request.session.get("basket", {})
    products = Product.objects.filter(id__in=basket.keys())
    items = []
    total = Decimal("0.00")
    for product in products:
        quantity = min(int(basket.get(str(product.id), 0)), product.stock)
        if quantity <= 0:
            continue
        localize_product(product, language)
        line_total = product.price * quantity
        total += line_total
        items.append({"product": product, "quantity": quantity, "line_total": line_total})
    return render(request, "store/basket.html", {"items": items, "total": total})


@require_POST
def update_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        quantity = int(request.POST.get("quantity", 1))
    except ValueError:
        quantity = 1

    basket = request.session.get("basket", {})
    if quantity <= 0:
        basket.pop(str(product_id), None)
    else:
        basket[str(product_id)] = min(quantity, product.stock)
    request.session["basket"] = basket
    messages.success(request, get_texts(request)["updated"])
    return redirect("basket")


@require_POST
def remove_from_basket(request, product_id):
    basket = request.session.get("basket", {})
    basket.pop(str(product_id), None)
    request.session["basket"] = basket
    messages.success(request, get_texts(request)["removed"])
    return redirect("basket")


def saved_items(request):  # Հեռացվել է @require_POST դեկորատորը
    language = get_language(request)
    saved = request.session.get("saved", [])
    products = Product.objects.filter(id__in=saved)
    products = [localize_product(item, language) for item in products]
    return render(request, "store/saved.html", {"products": products})


@require_POST
def save_for_later(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    saved = request.session.get("saved", [])
    if product.id not in saved:
        saved.append(product.id)
    request.session["saved"] = saved

    basket = request.session.get("basket", {})
    basket.pop(str(product.id), None)
    request.session["basket"] = basket
    messages.success(request, get_texts(request)["saved_message"])
    return redirect(safe_next_url(request, "saved_items"))


@require_POST
def remove_saved(request, product_id):
    saved = request.session.get("saved", [])
    if product_id in saved:
        saved.remove(product_id)
    request.session["saved"] = saved
    messages.success(request, get_texts(request)["removed"])
    return redirect("saved_items")


@require_POST
def checkout(request):
    basket = request.session.get("basket", {})
    products = Product.objects.filter(id__in=basket.keys())
    total = sum(
        (product.price * int(basket.get(str(product.id), 0)) for product in products),
        Decimal("0.00"),
    )
    if not basket:
        return redirect("basket")
    request.session["basket"] = {}
    return render(request, "store/checkout_success.html", {"total": total})