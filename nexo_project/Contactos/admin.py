from django.contrib import admin
from .models import Contact, Domicile, PhoneNumber, Country, Group

# Register your models here.
admin.site.register([Contact, Domicile, PhoneNumber, Country, Group])