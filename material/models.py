from django.db import models

# Create your models here.
class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_type = models.CharField(max_length=50, unique=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.material_type} ({self.material_id})"
