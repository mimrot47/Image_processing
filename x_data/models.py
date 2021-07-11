from django.db import models

# Create your models here.
gender_choice=(
    ('Male','male'),
    ('Femal','Femal')
)
covid=(
    ('Nagative','Nagative'),
    ('Positive','Positive')

)
class petaint(models.Model):
    ward_no= models.IntegerField(blank=True,null=True)
    bed_no=models.IntegerField(blank=True,null=True)
    Dr_name=models.CharField(max_length=50,blank=True)
    P_name = models.CharField(max_length=30)
    p_gender= models.CharField(max_length=30,choices=gender_choice)
    p_age=models.IntegerField()
    p_report=models.CharField(max_length=80 ,blank=True)
    blood_preshar=models.IntegerField(blank=True,null=True)
    Oxigen_leval=models.CharField(max_length=50,blank=True,null=True)
    Ventilator=models.BooleanField(default=False,null=True)
    Rendesiver_dose=models.IntegerField(null=True,blank=True)
    Eye_infection=models.CharField(max_length=50,null=True,blank=True)
    P_HRCT = models.CharField(max_length=30,blank=True)
    P_CRP = models.CharField(max_length=30,blank=True)
    p_covid=models.CharField(max_length=50,choices=covid,blank=True)
    P_per=models.IntegerField()
    P_x_image=models.ImageField(upload_to='images')
    # admission_date=models.DateTimeField(auto_now=False, auto_now_add=True,null=True)
    # updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    discharge=models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)


   
