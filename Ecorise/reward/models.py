from django.db import models
from product.models import Product
from users.models import User
class Reward(models.Model):
    reward_id = models.AutoField(max_length=10, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recycled_clothes = models.ForeignKey(Product, on_delete=models.CASCADE)
    rewards = models.CharField(max_length=100)
    rewards_at = models.DateTimeField()
    def __str__(self):
        return f"{self.reward_id}: {self.rewards}"
# Create your models here.
