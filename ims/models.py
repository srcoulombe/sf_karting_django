from django.db import models
from django.conf import settings
from django.utils import timezone 

class InventoryItem(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    last_updated = models.DateTimeField(default=timezone.now)
    in_stock = models.IntegerField()
    on_hold = models.IntegerField()
    price = models.FloatField()

    def post(self):
        self.last_updated = timezone.now()
        self.save()
    
    def __str__(self):
        return f"{self.title} for ${self.price} ({self.in_stock} items in stock, {self.on_hold} items on hold)"
