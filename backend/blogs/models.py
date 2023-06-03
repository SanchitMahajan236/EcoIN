from django.db import models
from general.models import UserDetails
from django.utils import timezone

# Create your models here.
#################################################
# BLOGS MODELS
#################################################
class Blogs(models.Model):
    Author = models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255,blank=False)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    views  =  models.CharField(max_length=100,blank=True)
    pay   =   models.CharField(max_length=5,blank=True)    
    class Meta:
        verbose_name = 'Blogs'
        verbose_name_plural=verbose_name
