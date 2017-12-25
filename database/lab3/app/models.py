from django.db import models
from django.utils import timezone


class Medic(models.Model):
    name = models.CharField(max_length = 30)
    lisense = models.CharField(max_length=30)
    about = models.CharField(max_length=30)
    cooperation = models.BooleanField()
    def dict(self):
        return {
            'name': self.name,
            'lisense': self.lisense,
            'about' : self.about,
            'coopertion': self.cooperation,
        }
    def __str__(self):
        return self.name

class Pharmacy(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    lisense = models.CharField(max_length=30)
    day_and_night = models.BooleanField()
    def dict(self):
        return {
            'name': self.name,
            'city': self.city,
            'lisense': self.lisense,
            'day_and_night': self.day_and_night,
        }
    def __str__(self):
        return self.name

class Pills(models.Model):
    name = models.CharField(max_length=30)
    consist = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    medic = models.ForeignKey(Medic,on_delete=None)
    pharmacy = models.ForeignKey(Pharmacy,on_delete=None)
    def dict(self):
        return {
            'name': self.name,
            'consist': self.consist,
            'price': self.price,
            'medic': self.medic,
            'pharmacy': self.pharmacy,

        }
