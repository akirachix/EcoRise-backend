from django.db import models
from trader.models import Trader
from recycler.models import Recycler

# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    trader_id= models.ForeignKey(Trader, on_delete = models.CASCADE)
    recycler_id= models.ForeignKey(Recycler, on_delete = models.CASCADE, null=True, blank= True)
    feedback_at = models.DateTimeField(auto_now_add = True)
    feedback = models.TextField(max_length = 500)

    def __str__(self):
        return f'Feedback {self.feedback_id}'
