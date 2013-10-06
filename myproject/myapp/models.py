from django.db import models

# Create your models here.

class List(models.Model):
    pass

class Item(models.Model):
    list = models.ForeignKey(List)
    text = models.TextField()

    class Meta:
        unique_together = ('list', 'text')
