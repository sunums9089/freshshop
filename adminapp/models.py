from django.db import models

# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField(default=0)
    product_image=models.ImageField(upload_to='productImage')