from xml.dom import ValidationErr
from django.db import models
from django.conf import settings
from django.utils import timezone 
from django.core.validators import MinValueValidator 

class InventoryItem(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    
    on_hold = models.PositiveIntegerField(default=0)
    in_stock = models.PositiveIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.0)])
    restocking_cost = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.0)])
    last_updated_on = models.DateTimeField(default=timezone.now)
    last_updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def _validate_in_stock(self):
        if self.in_stock < 0:
            raise ValidationErr("Cannot have fewer than 0 items in stock.")
    
    def _validate_on_hold(self):
        if self.on_hold < 0:
            raise ValidationErr("Cannot have fewer than 0 items on hold.")
    
    def _validate_price(self):
        if self.price < 0.0:
            raise ValidationErr("Price cannot be a negative value.")
    
    def _validate_restocking_cost(self):
        if self.restocking_cost < 0.0:
            raise ValidationErr("Restocking cost cannot be a negative value.")

    def save(self):
        self._validate_on_hold()
        self._validate_in_stock()
        self._validate_price()
        self._validate_restocking_cost()
        self.last_updated = timezone.now()
        return super().save()
    
    def __str__(self):
        return f"{self.title} for ${self.price} ({self.in_stock} items in stock, {self.on_hold} items on hold)"
