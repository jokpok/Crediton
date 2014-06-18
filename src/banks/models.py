from django.db import models
from crediton.settings import MEDIA_URL

class Bank(models.Model):
    
    name = models.CharField(max_length=200)
    site = models.CharField(max_length=100)
    phones = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='logos/')
    rating = models.IntegerField(null=True, blank=True)
    
    def get_logo_url(self):
        
        return MEDIA_URL + str(self.logo)
    
    def __unicode__(self):
        return str(self.name.encode("utf-8"))


    
