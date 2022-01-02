# Generated by Django 3.2 on 2021-12-15 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concesionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ubicacion', models.CharField(max_length=30)),
                ('TlfConce', models.IntegerField()),
                ('Horario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=9)),
                ('NumTlf', models.IntegerField()),
                ('Direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.CharField(max_length=30)),
                ('Modelo', models.CharField(max_length=30)),
                ('Color', models.CharField(max_length=11)),
                ('Extras', models.CharField(max_length=100)),
                ('Stock', models.CharField(max_length=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Concesionarioco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionario_app.concesionario')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pedido', models.ManyToManyField(to='concesionario_app.Coche')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionario_app.usuario')),
            ],
        ),
    ]