from django.db import models
#from phone_field import PhoneField
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
#farmer table


class Farmer(models.Model):
    farmer_name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    aadhar_no = models.BigIntegerField()
    mpin = models.IntegerField()

    def __str__(self):
        return self.farmer_name

#Agriculture Expert


class AgriExpert(models.Model):

    expert_name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    aadhar_no = models.BigIntegerField()
    mpin = models.IntegerField()
    occupation = models.CharField(max_length= 25)
    field_of_interest = models.CharField(max_length=25)

    def __str__(self):
        return self.expert_name


class AgriAssistant(models.Model):

    assistant_name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    aadhar_no = models.BigIntegerField()
    mpin = models.IntegerField()
    taluka = models.CharField(max_length= 25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.assistant_name

class States(models.Model):

    #state_id = models.IntegerField(max_length=11,blank=False)
    state_name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.state_name


class Cities(models.Model):
   # city_id = models.IntegerField(blank=False, auto_created=True)
    city_name = models.CharField(max_length=30, blank=False)
    state_id = models.ForeignKey(States,on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name
        #return '{}'.format(self.city_name)

    #
class Talukas(models.Model):
   # city_id = models.IntegerField(blank=False, auto_created=True)
    taluka_name = models.CharField(max_length=30, blank=False)
    city_id = models.ForeignKey(Cities,on_delete=models.CASCADE)

    def __str__(self):
        return self.taluka_name


