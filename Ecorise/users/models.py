from django.db import models
USER_TYPE_CHOICES = [('Trader','trader'),('recycler','Recycler')]
class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100,unique = True,null = True,blank = True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.CharField(max_length=50, choices=[('recycler', 'Recycler'), ('traders', 'trader')], blank=True, null=True)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.user_id} - {self.name}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(email__isnull=False) | models.Q(phone__isnull=False),
                name='email_or_phone_check'
            ),]
    





