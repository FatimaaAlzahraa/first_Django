from django.contrib import admin
from .models import ApparelSize,ProductColor,Product,ProductCategories
# Register your models here.
admin.site.register(ApparelSize)
admin.site.register(ProductColor)
admin.site.register(Product)
admin.site.register(ProductCategories)
# admin.site.register(Categories)