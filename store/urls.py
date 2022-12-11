from django.urls import path
from . import views

app_name = "store"  #this means we don't have to hardcode the url, keep it the same as our App name ("main" directory))

urlpatterns = [
    path("products/", views.product_page, name="Product page"),
    path("admin_page/", views.admin_page, name="admin_page"),
]
