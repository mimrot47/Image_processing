from django.forms import ModelForm
from .models import petaint


class pataintForm(ModelForm):
    
    class Meta:
        model = petaint
        fields = '__all__'
