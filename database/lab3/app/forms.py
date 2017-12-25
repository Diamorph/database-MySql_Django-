from django.forms import ModelForm
from .models import Pharmacy, Medic, Pills

class PharmacyForm(ModelForm):
    class Meta:
        model = Pharmacy
        fields = ['name' , 'city' , 'lisense' , 'day_and_night']

class MedicForm(ModelForm):
    class Meta:
        model = Medic
        fields = ['name','lisense','about','cooperation']

class PillsForm(ModelForm):
    class Meta:
        model = Pills
        fields = ['name','consist','price','medic','pharmacy']

