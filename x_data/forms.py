from django.forms import ModelForm
from .models import petaint
from django.contrib.auth.models import User


class pataintForm(ModelForm):
    class Meta:
        model = petaint
        # fields = ['ward_no','bed_no','Dr_name','P_name','p_gender','p_age','p_report','blood_preshar','Oxigen_leval','Ventilator','Rendesiver_dose','P_x_image','P_per']
        fields="__all__"

class SignUpForm(ModelForm):
    
    class Meta:
        model = User
        fields=['username','password','email','first_name','last_name']