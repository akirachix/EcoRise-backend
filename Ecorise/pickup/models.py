from django.db import models

from material_pricing.models import Material
from recycler.models import Recycler
from trader.models import Trader

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    material = models.ForeignKey(Material, on_delete =models.CASCADE)
    trader = models.ForeignKey(Trader, on_delete = models.CASCADE)
    recycler = models.ForeignKey(Recycler, on_delete = models.CASCADE)
    trader_name = models.CharField(max_length = 255)
    phone_number = models.IntegerField(unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    latitude = models.DecimalField(max_digits = 9, decimal_places = 6)
    longitude = models.DecimalField(max_digits = 9, decimal_places = 6)
    pickup_status = models.CharField(max_length = 50, choices = [("Pending", "Pending"), ("Confirmed", "Confirmed")])
    pickup_at = models.DateTimeField(null = True, blank = True)
    
    def __str__(self):
        return f"{self.request_id }"
