from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from product.models import Product


def product_manage(request):
    username = request.session.get("user", "")
    product_list = Product.objects.all()
    return render(request, "product_manage.html", {
        "user": username,
        "products": product_list
    })


@login_required
def product_search(request):
    username = request.session.get("user", "")
    search_productname = request.GET.get("productname", "")
    product_list = Product.objects.filter(product_name__icontains=search_productname)
    return render(request, "product_manage.html", {
        "user": username,
        "product": product_list
    })