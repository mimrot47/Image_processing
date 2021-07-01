from django.contrib import admin
from .models import petaint

# Register yourlist_display = 

@admin.register(petaint)
class petaintAdmin(admin.ModelAdmin):
    list_display=['id','P_name','p_gender','p_age','p_covid','P_per','P_x_image']

