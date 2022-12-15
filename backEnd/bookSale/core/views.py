from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import GetAllProduct
from django.http import JsonResponse
import random
# Home
def getPromoProduct(request):
        obj = Product.objects.all().order_by('product_id')[:6] 

        data = { "result" :list(obj.values("product_id", "category_id", "prodcut_num", "product_intro", "product_name", "product_picture","product_price","product_title"))
                }
        
        return JsonResponse(data)
        
def getCategory(request):
        pass
def getProductByCategory(request):
        pass 

# Goods (All product)
def getAllProduct(request):
        obj = Product.objects.all()
        data = { "result" :list(obj.values("product_id", "category_id", "prodcut_num", "product_intro", "product_name", "product_picture","product_price","product_title"))
                }
        
        return JsonResponse(data)

def getProductByCategory(request):
        pass
def getProductBySearch(request):
        pass
 # Details 
def getDetails(request):
        pass
def getDetailsPicture(request):
        pass
def addShoppingCart(request):
        pass
def addCollect(request):
        pass
# Order 
def getOrder(request):
        pass
# shoppingCart
def updateShoppingCart(request):
        pass
def deleteShoppingCart(request):
        pass
#confirmOrder
def addOrder(request):
        pass
# Collection
def getCollect(request):
        pass
# register
def register(request):
        pass
# login
def login(request):
        pass

# MyList 
def deleteCollect(request):
        pass