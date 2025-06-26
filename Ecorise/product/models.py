from django.db import models

# Create your models here.
class Product(models.Model):
   product_id = models.AutoField(primary_key=True)
   quantity = models.IntegerField()
   type = models.CharField(max_length=50)
   price = models.IntegerField()
   listed_at = models.DateTimeField()
   def __str__(self):
       return f"{self.type} (ID: {self.product_id})"
