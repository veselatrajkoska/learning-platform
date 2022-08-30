from django import forms
from .models import PlatformUser

class PlatformUserForm(forms.ModelForm):
    class Meta:
        model = PlatformUser
        exclude = ('user', )

DEMO_CHOICES = (
    ("1", "Naveen"),
    ("2", "Pranav"),
    ("3", "Isha"),
    ("4", "Saloni"),
)

class GeeksForm(forms.Form):
    geeks_field = forms.MultipleChoiceField(choices = DEMO_CHOICES)
