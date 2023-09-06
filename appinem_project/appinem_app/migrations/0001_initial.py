# Generated by Django 4.2.5 on 2023-09-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tarjeta_identidad', models.CharField(max_length=20)),
                ('Clave', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cedula', models.CharField(max_length=20)),
                ('Clave', models.CharField(max_length=100)),
            ],
        ),
    ]