from django.shortcuts import render
from .models import Product

def product_page(request):
    return render(request=request, template_name="products.html",
    context={"products": Product.objects.all}
                 )

def admin_page(request):
    return render(request=request, template_name="admin_page.html")