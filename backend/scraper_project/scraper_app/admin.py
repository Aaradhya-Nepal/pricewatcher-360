# scraper/admin.py
from django.contrib import admin
from .models import ScrapedProduct

admin.site.register(ScrapedProduct)
