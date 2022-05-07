from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()
    city = models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)
    investment = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.name