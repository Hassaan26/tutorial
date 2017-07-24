from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(default=False, max_length=200)
    product_description = models.TextField(default=False, max_length=200)
    product_category = models.CharField(max_length=100)
    product_tag = models.CharField(default=False, max_length=50)
    pub_date = models.DateTimeField('date published')
    product_img = models.ImageField(max_length=300)
    product_price = models.CharField(max_length=30000, default=False)
    product_status = models.BooleanField(default=True)