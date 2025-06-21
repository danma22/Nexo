from django.urls import path
from . import views

urlpatterns = [
    path('', views.organizador, name='organizador'),
    path('crear-tarea/', views.create_task, name='crear-tarea'),
    path('editar-tarea/<int:pk>/', views.update_task, name='editar-tarea'),
    path('tareas/<int:pk>/', views.show_task, name='ver-tarea'),
    path('borrar-tarea/<int:pk>/', views.delete_task, name='borrar-tarea'),
    path('archivar-tarea/<int:pk>/', views.archive_task, name='archivar-tarea'),
    path('crear-categoria/', views.create_category, name='crear-categoria'),
    path('borrar-categoria/', views.delete_category, name='borrar-categoria'),
    path('archivados/', views.show_archive_tasks, name='archivados')
]