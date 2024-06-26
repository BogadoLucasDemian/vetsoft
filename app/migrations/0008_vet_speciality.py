# Generated by Django 5.0.4 on 2024-05-22 03:07

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_vet_alter_medicine_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='vet',
            name='speciality',
            field=models.CharField(choices=[('Oftalmologia', 'Oftalmología'), ('Quimioterapia', 'Quimioterapia'), ('Radiologia', 'Radiología'), ('Ecocardiografias', 'Ecocardiografías'), ('Traumatologia', 'Traumatología'), ('Ecografias', 'Ecografías'), ('Urgencias', 'Urgencias')], default=app.models.Speciality['Urgencias'], max_length=100),
        ),
    ]
