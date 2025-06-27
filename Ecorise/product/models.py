from django.db import models

# Create your models here.


class Product(models.Model):
   product_id = models.AutoField(primary_key=True)
   quantity = models.IntegerField()
   product_name = models.CharField(max_length=10)
   type = models.CharField(max_length=50)
   price = models.IntegerField()
   listed_at = models.DateTimeField()
   def __str__(self):
       return f"{self.type} (ID: {self.product_id})"



class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_type = models.CharField(max_length=50, unique=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.material_type} ({self.material_id})"
