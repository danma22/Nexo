from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactos, name='contactos'),
    path('<int:pk>/', views.show_contact, name='ver-contacto'),
    path('crear-contacto/', views.create_contact, name='crear-contacto'),
    path('editar-contacto/<int:pk>/', views.update_contact, name='editar-contacto'),
    path('borrar-contacto/<int:pk>/', views.delete_contact, name="borrar-contacto"),
    path('borrar-domicilio/<int:pk>/<int:domicile_id>/', views.delete_domicile, name='borrar-domicilio'),
    path('borrar-telefono/<int:pk>/<int:phone_id>/', views.delete_phone, name='borrar-telefono'),
    path('crear-grupo/', views.create_group, name='crear-grupo'),
    path('borrar-grupo/', views.delete_group, name='borrar-grupo')
]