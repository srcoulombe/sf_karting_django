import os
import base64
from io import BytesIO  

from PIL import Image

from xml.dom import ValidationErr
from django.db import models
from django.conf import settings
from django.utils import timezone 
from django.core.validators import MinValueValidator 

class InventoryItem(models.Model):
    title = models.CharField(max_length=256, unique=True)
    description = models.TextField(default="", blank=True, null=True)
    
    on_hold = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    in_stock = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)])
    
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.0)])
    restocking_cost = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.0)])
    min_quantity_in_stock = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0.0)])

    user_uploaded_image = models.ImageField(upload_to='images/', default='images/karting.jpg')

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

    def _validate_min_quantity_in_stock(self):
        if self.min_quantity_in_stock < 0:
            raise ValidationErr("Minimum quantity in stock cannot be a negative value.")
    
    def _validate_needs_restocking(self):
        pass
        
    @property
    def thumbnail_base64_image_str(self):
        thumbnail_size = 100, 100
        data_img = BytesIO()
        tiny_img = Image.open(self.user_uploaded_image)
        tiny_img.thumbnail(thumbnail_size)
        tiny_img.save(data_img, format="BMP")
        tiny_img.close() 
        thumbnail_base64_image_str_ = "data:image/jpg;base64,{}".format(
            base64.b64encode(data_img.getvalue()).decode("utf-8")
        )
        return thumbnail_base64_image_str_

    @property
    def needs_restocking(self):
        if (self.in_stock - self.on_hold) < self.min_quantity_in_stock:
            return True
        else:
            return False

    def save(self):
        self._validate_on_hold()
        self._validate_in_stock()
        self._validate_price()
        self._validate_restocking_cost()
        self._validate_min_quantity_in_stock()
        self._validate_needs_restocking()
        _ = self.thumbnail_base64_image_str
        self.last_updated = timezone.now()
        return super().save()
    
    def __str__(self):
        return f"{self.title} for ${self.price} ({self.in_stock} items in stock, {self.on_hold} items on hold)"
