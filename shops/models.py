from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)

class Listing(models.Model):
    shop = models.ForeignKey(Shop, related_name='listings', on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True, blank=True, )
    description = models.TextField(null=True, blank=True, max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True),
    quantity = models.PositiveBigIntegerField(max_length=10,null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


