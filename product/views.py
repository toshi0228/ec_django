from django.shortcuts import render
from django.http import HttpResponse
from .models import Plan

# Create your views here.

def provisional(request):
    return HttpResponse("hello world!!")


def product_list(request):
    plans = Plan.objects.order_by('name')
    return render (request,'index.html', {'plans': plans})



# ＝＝＝＝＝＝＝＝＝見本＝＝＝＝＝＝＝＝＝


# def plan_list(request):
#     plans = Plan.objects.order_by('name')
#     return TemplateResponse(request, 'catalogue/product_list.html',
#                             {'products': products})


# def product_detail(request, product_id):
#     try:
#         product = Product.objects.get(id=product_id)
#     except Product.DoesNotExist:
#         raise Http404
#     return TemplateResponse(request, 'catalogue/product_detail.html',
#                             {'product': product})
