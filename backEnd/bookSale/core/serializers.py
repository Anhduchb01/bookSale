from rest_framework import serializers


from .models import Product
class GetProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['product_id','category_id','prodcut_num','product_intro','product_name','product_picture','product_price','product_title']