
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        #home
        path('product/getPromoProduct',getPromoProduct,name='getPromoProduct'),
        path('product/getProductByCategory',getProductByCategory,name='getProductByCategory'),
        path('product/getCategory',getCategory,name='getCategory'),
        #good ( all product )
        path('product/getAllProduct',getAllProduct,name='getAllProduct'),
        path('product/getProductByCategory',getProductByCategory,name='getProductByCategory'),
        path('product/getProductBySearch',getProductBySearch,name='getProductBySearch'),
        #details
        path('product/getDetails',getDetails,name='getDetails'),
        path('product/getDetailsPicture',getDetailsPicture,name='getDetailsPicture'),
        path('user/shoppingCart/addShoppingCart',addShoppingCart,name='addShoppingCart'),
        path('user/collect/addCollect',addCollect,name='addCollect'),
        # Order 
        path('user/order/getOrder',getOrder,name='getOrder'),
        # shoppingCart
        path('user/shoppingCart/updateShoppingCart',updateShoppingCart,name='updateShoppingCart'),
        path('user/shoppingCart/deleteShoppingCart',deleteShoppingCart,name='deleteShoppingCart'),
        # ConfirmOrder
        path('user/order/addOrder',addOrder,name='addOrder'),
        # Collection
        path('user/collect/getCollect',getCollect,name='getCollect'),
        # login
        path('users/login',login,name='login'),
        # register
        path('users/register',register,name='register'),
        # MyList 
        path('user/collect/deleteCollect',deleteCollect,name='deleteCollect'),


]