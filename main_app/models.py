from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.

FUEL = (
    ('M', 'morning fueling'),
    ('A', 'afternoon fueling'),
    ('E', 'evening fueling'),
)

class Car(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    engine = models.CharField(max_length=1100)
    
    def fueled_for_today(self):
        return self.fueling_set.filter(date=date.today()).count() >= len(FUEL)

    def __str__(self):
        return f'{self.make} {self.model}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})
    
class Fueling(models.Model):
    date = models.DateField('Fueling Date')
    fuel = models.CharField(
        max_length=1,
        choices=FUEL,
        default=FUEL[2][0]
        )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.get_fuel_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
    