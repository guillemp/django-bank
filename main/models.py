from django.db import models
from decimal import Decimal

class Account(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=64)

class Category(models.Model):
    name = models.CharField(max_length=64)
    icon = models.CharField(max_length=32)
    
class Transaction(models.Model):
    account = models.ForeignKey(Account)
    description = models.CharField(max_length=240)
    date = models.DateField(null=True, blank=True)
    more = models.CharField(max_length=240)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    category = models.ForeignKey(Category, blank=True, null=True)
    hash_code = models.CharField(max_length=128)
    
    def url(self):
        return "/transaction/{}/".format(self.id)