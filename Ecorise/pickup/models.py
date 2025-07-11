from django.db import models
from material.models import Material
from users.models import User

class Pickup(models.Model):
    request_id = models.AutoField(primary_key=True)
    material = models.ForeignKey(Material, on_delete =models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    market_location = models.CharField(max_length = 100,default=1)
    market_latitude = models.DecimalField(max_digits = 9, decimal_places = 6)
    market_longitude = models.DecimalField(max_digits = 9, decimal_places = 6)
    pickup_status = models.CharField(max_length = 50, choices = [("Pending", "Pending"), ("Confirmed", "Confirmed")])
    pickup_at = models.DateTimeField(null = True, blank = True)
   
    def __str__(self):
        return self.request_id 

