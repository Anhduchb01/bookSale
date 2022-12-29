from django.contrib import admin
from .models import Product, User , Rating , Category , ShoppingCart,Order,Author,Rating_Author
# Register your models here.
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Category)
admin.site.register(ShoppingCart)
admin.site.register(Order)
admin.site.register(Author)
admin.site.register(Rating_Author)
