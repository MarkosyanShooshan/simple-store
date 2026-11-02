from .models import Product
from .translations import LANGUAGES, get_language, get_texts


def store_context(request):
    basket = request.session.get("basket", {})
    saved = request.session.get("saved", [])

    basket_count = sum(int(quantity) for quantity in basket.values())
    saved_count = Product.objects.filter(id__in=saved).count() if saved else 0

    return {
        "t": get_texts(request),
        "current_language": get_language(request),
        "languages": LANGUAGES,
        "basket_count": basket_count,
        "saved_count": saved_count,
    }


"""
This context processor makes common store information available
in every template: translations, current language, available
languages, basket item count, and saved product count.
"""