from django.db import models

from banks.models import Bank

CURRENT_CHOICES = (
    ('USD', 'USD'),
    ('KZT', 'KZT'),
    ('EUR', 'EUR'),
)

class Credit(models.Model):
    
    bank = models.ForeignKey(Bank)
    name = models.CharField(max_length=200)
    currency = models.CharField(choices=CURRENT_CHOICES, max_length=3)
    max_sum = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    min_sum = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    percent_years = models.DecimalField(max_digits=100, decimal_places=2)
    gasv = models.DecimalField(max_digits=100, decimal_places=2)
    term = models.IntegerField(null=True, blank=True)
    


   
#class Commission(models.Model):
    
 #   credit = models.ForeignKey(Credit)
  #  consideration = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
   # arrangement = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    #cash_fee = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)


