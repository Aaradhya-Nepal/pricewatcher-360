# scraper/admin.py
from django.contrib import admin
from .models import ScrapedProduct
from .models import ProductDetail
from .models import TrackerUser

admin.site.register(ScrapedProduct)
admin.site.register(ProductDetail)
admin.site.register(TrackerUser)