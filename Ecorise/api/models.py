from django.db import models

from decimal import Decimal
from django.utils import timezone

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('M-Pesa', 'M-Pesa'),
        ('Bank', 'Bank Transfer'),
        ('Cash', 'Cash'),
    ]
    
    payment_id = models.AutoField(primary_key=True, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    points_award = models.CharField(max_length=10)
    payment_method = models.CharField(
        max_length=30, 
        choices=PAYMENT_METHOD_CHOICES,
        default='M-Pesa'
    )
    payment_status = models.CharField(
        max_length=30, 
        choices=PAYMENT_STATUS_CHOICES,
        default='Pending'
    )
    phone_number = models.CharField(max_length=15)  # Changed to CharField
    mpesa_receipt_number = models.CharField(max_length=100, blank=True, null=True)
    paid_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ['-paid_at']
    
    def __str__(self):
        return f"{self.payment_id} | {self.phone_number} | {self.amount} {self.payment_status}"





# Create your models here.
