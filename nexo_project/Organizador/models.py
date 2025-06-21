from django.db import models
from datetime import date, datetime

class Status(models.Model):
    status_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.ForeignKey(Status, default=1, on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title