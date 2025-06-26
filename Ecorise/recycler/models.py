from django.db import models

# Create your models here.
class Recycler(models.Model):
   recycler_id = models.CharField(
       max_length=10,
       primary_key=True,
       unique=True,
   )
   name = models.CharField(
       max_length=100,
       help_text="Full name of the user"
   )
   email = models.EmailField(
       max_length=100,
       unique=True,
       null=True,
       blank=True,
       help_text="Unique, nullable email address"
   )
   phone_number = models.IntegerField(
       unique=True,
       null=True,
       blank=True,
       help_text="Unique, nullable phone number"
   )
   password = models.CharField(
       max_length=100,
       help_text="Encrypted password"
   )
   created_at = models.DateTimeField(
       auto_now_add=True,
       help_text="Account creation timestamp"
   )
   def __str__(self):
       return f"{self.name} ({self.recycler_id})"
