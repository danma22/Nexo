from django.db import models

class Country(models.Model):
    country_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    code_flag = models.CharField(max_length=5, default='')
    
    def __str__(self):
        return self.name

class Domicile(models.Model):
    domicile_id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.address + ' ' + self.city + ' ' + self.country.name
    
class PhoneNumber(models.Model):
    phone_id = models.BigAutoField(primary_key=True)
    country_code = models.CharField(max_length=5, blank=True, null=False)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.phone_number
    
class Group(models.Model):
    group_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    contact_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name_p = models.CharField(max_length=50)
    last_name_m = models.CharField(max_length=50)
    phone_number = models.ForeignKey(PhoneNumber, blank=True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(max_length=50)
    discord_account = models.URLField(blank=True, null=False, default='')
    github_account = models.URLField(blank=True, null=False, default='')
    domicile = models.ForeignKey(Domicile, blank=True, null=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name + ' ' + self.last_name_p
