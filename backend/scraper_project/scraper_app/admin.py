# scraper/admin.py
from django.contrib import admin
from .models import ScrapedProduct
from .models import Product

admin.site.register(ScrapedProduct)
admin.site.register(Product)