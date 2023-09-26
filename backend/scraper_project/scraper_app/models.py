# scraper/models.py
from django.db import models

class ScrapedProduct(models.Model):
    title = models.CharField(max_length=200)
    current_price = models.CharField(max_length=20)
    original_price = models.CharField(max_length=20)
    discount = models.CharField(max_length=20)
    image = models.URLField()
    link = models.URLField()
    alt_text = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    number_of_reviews = models.IntegerField()

    def __str__(self):
        return self.title
