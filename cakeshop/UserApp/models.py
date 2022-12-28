from django.db import models
from AdminApp.models import Product,UserInformation

# Create your models here.


class MyCart(models.Model):
    user = models.ForeignKey(to='AdminApp.UserInformation', on_delete= models.CASCADE)
    cake = models.ForeignKey(to='AdminApp.Product', on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table="MyCart"
