from django.urls import path
from .import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<int:product_id>/", views.product_detail,name="product_detail"),
    path("language/<str:language>/",views.set_language,name="set_language"),
    path("basket/", views.basket_view, name="basket"),
    path("basket/add/<int:product_id>/",views.add_to_basket,name="add_to_basket"),
    path("basket/update/<int:product_id>/",views.update_basket,name="update_basket"),
    path("basket/remove/<int:product_id>/",views.remove_from_basket,name="remove_from_basket"),
    path("saved/", views.saved_items, name = "saved_items"),
    path("saved/add/<int:product_id>/",views.save_for_later, name="save_for_later"),
    path("saved/remove/<int:product_id>/",views.remove_saved, name="remove_saved"),
    path("checkout/",views.checkout, name="checkout"),


]