from django.db import models


# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    engine = models.CharField(max_length=1100)

    def __str__(self):
        return f'{self.make} {self.model}'
    
