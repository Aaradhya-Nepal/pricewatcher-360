# scraper/admin.py
from django.contrib import admin
from .models import ScrapedProduct
from .models import Product
from .models import ProductDetail

admin.site.register(ScrapedProduct)
admin.site.register(Product)
admin.site.register(ProductDetail)