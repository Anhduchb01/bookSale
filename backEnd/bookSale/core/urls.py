
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        path('user/recommend',recommend,name='recommend_cf'),

        #home
        path('product/getPromoProduct',getPromoProduct,name='getPromoProduct'),
        path('product/getProductByCategory',getProductByCategory,name='getProductByCategory'),
        path('product/getCategory',getCategory,name='getCategory'),
        path('user/shoppingCart/getShoppingCart',getShoppingCart,name='getShoppingCart'),

        #good ( all product )
        path('product/getAllProduct',getAllProduct,name='getAllProduct'),
        path('product/getProductBySearch',getProductBySearch,name='getProductBySearch'),
        #details
        path('product/getDetails',getDetails,name='getDetails'),
        path('user/shoppingCart/addShoppingCart',addShoppingCart,name='addShoppingCart'),
        path('user/voteStar',voteStar,name='voteStar'),

        # shoppingCart
        path('user/shoppingCart/updateShoppingCart',updateShoppingCart,name='updateShoppingCart'),
        path('user/shoppingCart/deleteShoppingCart',deleteShoppingCart,name='deleteShoppingCart'),
        # Order

        path('user/order/addOrder',addOrder,name='addOrder'),
        # login
        path('users/login',login,name='login'),
        # register
        path('users/register',register,name='register'),
        path('users/findUserName',findUserName,name='findUserName'),
]