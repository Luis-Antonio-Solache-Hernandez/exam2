from django import forms
from main.models import Twitt, Zombie


class TwittForm(forms.ModelForm):
    class Meta:
        model = Twitt


class ZombieForm(forms.ModelForm):
    class Meta:
        model = Zombie
