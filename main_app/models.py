from django.db import models
from django.urls import reverse


# Create your models here.

TRAN = (
    ('2A', '2spd automatic'),
    ('3A', '3spd automatic'),
    ('3M', '3spd manual'),
    ('4M', '4spd manual')
)

class Car(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    engine = models.CharField(max_length=1100)

    def __str__(self):
        return f'{self.make} {self.model}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})
    
class Transmission(models.Model):
    tran = models.CharField(
        max_length=2,
        choices=TRAN,
        default=TRAN[1][0]
        )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"This beauty runs with a {self.get_tran_display()}"
    
    