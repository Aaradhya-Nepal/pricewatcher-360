# scraper/models.py
from django.db import models

class ScrapedProduct(models.Model):
    title = models.CharField(max_length=200)
    current_price = models.CharField(max_length=20)
    original_price = models.CharField(max_length=20)
    discount = models.CharField(max_length=20)
    image = models.URLField()
    link = models.URLField(unique=True)
    alt_text = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    number_of_reviews = models.IntegerField()

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=20, null=True, blank=True)
    delivery_info = models.CharField(max_length=255, null=True, blank=True)
    sold_by = models.CharField(max_length=255, null=True, blank=True)
    positive_seller_ratings = models.CharField(max_length=20, null=True, blank=True)
    ship_on_time = models.CharField(max_length=20, null=True, blank=True)
    chat_response_rate = models.CharField(max_length=20, null=True, blank=True)
    highlights = models.TextField(null=True, blank=True)
    brand_spec = models.CharField(max_length=100, null=True, blank=True)
    sku_spec = models.CharField(max_length=50, null=True, blank=True)
    image_links = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class ProductDetail(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=20, null=True, blank=True)
    delivery_info = models.CharField(max_length=255, null=True, blank=True)
    sold_by = models.CharField(max_length=255, null=True, blank=True)
    positive_seller_ratings = models.CharField(max_length=20, null=True, blank=True)
    ship_on_time = models.CharField(max_length=20, null=True, blank=True)
    chat_response_rate = models.CharField(max_length=20, null=True, blank=True)
    highlights = models.TextField(null=True, blank=True)
    brand_spec = models.CharField(max_length=100, null=True, blank=True)
    sku_spec = models.CharField(max_length=50, null=True, blank=True)
    image_links = models.JSONField(null=True, blank=True)
    scraped_product_link = models.OneToOneField(ScrapedProduct, on_delete=models.CASCADE, to_field='link',unique=True)

    def __str__(self):
        return self.title

