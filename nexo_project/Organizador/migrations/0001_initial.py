# Generated by Django 5.2 on 2025-06-06 21:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


def insert_status_values(apps, schema_editor):
    Status = apps.get_model('Organizador', 'Status')
    Status.objects.bulk_create([
        Status(name='Pendiente', color='orange'),
        Status(name='Completado', color='blue')
    ])

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Organizador.category')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Organizador.status')),
            ],
        ),
        migrations.RunPython(insert_status_values)
    ]
