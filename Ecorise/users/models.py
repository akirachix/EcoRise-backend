from django.db import models

class Trader(models.Model):
    trader_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100,unique = True,null = True,blank = True)
    phone_number = models.IntegerField(unique = True,null = True,blank = True)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.trader_id} - {self.name}"


class Recycler(models.Model):
   recycler_id = models.CharField(max_length=10,primary_key=True, unique=True )
   name = models.CharField(max_length=100)
   email = models.EmailField(max_length=100,unique=True,null=True,blank=True)
   phone_number = models.IntegerField( unique=True,null=True,blank=True)
   password = models.CharField( max_length=100 )
   created_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
       return f"{self.name} ({self.recycler_id})"



