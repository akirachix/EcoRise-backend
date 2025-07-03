from django.db import models
from users.model import User

# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    trader = models.ForeignKey(User, on_delete = models.CASCADE)
    recycler = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add = True)
    feedback = models.TextField(max_length = 500)

    

    def __str__(self):
        return f'Feedback {self.feedback_id}'
