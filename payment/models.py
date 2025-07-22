from django.db import models
from material.models import Material
from users.models import User
from decimal import Decimal
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True, unique=True)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    points_award = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=30, default='M-Pesa')
    payment_status = models.CharField(max_length=30, choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Failed', 'Failed')])
    phone_number = models.IntegerField()
    mpesa_receipt_number = models.CharField(max_length=100)
    paid_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.payment_id} | {self.trader} | {self.amount} {self.payment_status}"

# Create your models here.
