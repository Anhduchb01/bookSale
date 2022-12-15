from django.db import models

# Create your models here.
from distutils.command.upload import upload


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField(blank=True, null=True)
    prodcut_num = models.IntegerField(blank=True, null=True)
    product_intro = models.TextField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    product_picture = models.TextField(blank=True, null=True)
    product_price = models.IntegerField(blank=True, null=True)
    product_title = models.TextField(blank=True, null=True)

    class Meta:
	
        managed = False
        db_table = 'product'
        ordering = ['product_id']

    def __str__(self) -> str:
                return str(self.product_id) + " -- " + str(self.product_name)
class User(models.Model):
	password = models.CharField(blank=True, null=True,max_length=20)
	user_id = models.IntegerField(primary_key=True)
	user_name = models.CharField(blank=True, null=True , max_length=100)
	class Meta:
		managed = False
		db_table = 'user'
		ordering = ['user_id']
	def __str__(self) -> str:
		return str(self.user_id) + "--" + str(self.user_name)

class Rating(models.Model):
	rating_id = models.IntegerField(primary_key=True)
	product_id = models.IntegerField(blank=False, null=False)
	user_id = models.IntegerField(blank=False, null=False)
	rating = models.IntegerField(blank=True, null=True)
	
	class Meta:
		managed = False
		db_table = 'rating'
	def __str__(self) -> str:
		return "Rating of user_id " + str(self.user_id)+ " for product_id "+str(self.product_id) 

class Category(models.Model):
	category_id = models.IntegerField(primary_key=True)
	category_name = models.CharField(blank=True, null=True,max_length=100)
	class Meta:
		managed = False
		db_table = 'category'
		ordering = ['category_id']
	def __str__(self) -> str:
		return str(self.category_id) + " -- " + str(self.category_name)

