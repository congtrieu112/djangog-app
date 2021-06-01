from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class ProductHistory(models.Model):
    date_create_at = models.DateTimeField(auto_now_add=True)
    date_update_at= models.DateTimeField(auto_now_add=True)
    image=models.TextField(max_length=500)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    content = TextField(max_length=10000)
    description = TextField(max_length=5000)
