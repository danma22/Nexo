from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contactos/', include('Contactos.urls')),
    path('organizador/', include('Organizador.urls'))
]
