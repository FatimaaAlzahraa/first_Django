from django.db import models

# Create your models here.

class ApparelSize(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_code = models.CharField(max_length=100)
    other_data = models.CharField(max_length=100,null=False)
    def __str__(self) :
        return self.size_code

class ProductColor(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_code = models.CharField(max_length=100)
    color_name = models.CharField(max_length=100)
    def __str__(self) :
        return self.color_name 


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_id = models.AutoField(primary_key=True )
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE , null=False)
    size = models.ForeignKey(ApparelSize, on_delete=models.CASCADE, null=False,blank=False )
    def __str__(self) :
        return self.product_name

class ProductCategories(models.Model):
    category_id = models.AutoField(primary_key=True)
    # category_id_parent = models
    category_name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE , null=False )
    def __str__(self) :
        return self.category_name

# class Categories(models.Model):
#     category_id = models.AutoField(primary_key=True)
#     category_name = models.CharField(max_length=100)
#     product_categories = models.OneToOneField(ProductCategories, on_delete=models.CASCADE )
