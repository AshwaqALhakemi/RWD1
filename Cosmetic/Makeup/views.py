from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'makeup/index.html')

# def brand_list(request):
#     return HttpResponse("brand list")

# def product_list(request):
#     return HttpResponse("product_list")

# def brand_details(request):
#     return HttpResponse("brand_details")

# def product_details(request):
#     return HttpResponse("product_details")



