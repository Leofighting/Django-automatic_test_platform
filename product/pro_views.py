from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from product.models import Product


def product_manage(request):
    username = request.session.get("user", "")
    product_list = Product.objects.all()
    product_count = product_list.count()
    paginator = Paginator(product_list, 5)
    page = request.GET.get("page", 1)
    currentPage = int(page)
    try:
        product_list = paginator.page(currentPage)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)
    return render(request, "product_manage.html", {
        "user": username,
        "products": product_list,
        "productcounts": product_count
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