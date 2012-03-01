from django import forms
from main.models import Zombie


class ZombieForm(forms.ModelForm):
    class Meta:
        model = Zombie
