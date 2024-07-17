from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Listing(models.Model):
    shop_id = models.ForeignKey(Shop, related_name='listings', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title if self.title else f"Listing {self.id}"
