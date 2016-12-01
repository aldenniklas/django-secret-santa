from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models

# Create your models here.

class Santa(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    wishlist = models.TextField(blank=True)
    restrictions = models.CharField(max_length=200, blank=True)
    
class SantaForm(ModelForm):
    class Meta:
        model = Santa
        fields = '__all__'
    
    
