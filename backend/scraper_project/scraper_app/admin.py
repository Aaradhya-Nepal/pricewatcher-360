# scraper/admin.py
from django.contrib import admin
from .models import ScrapedProduct
from .models import ProductDetail

admin.site.register(ScrapedProduct)
admin.site.register(ProductDetail)