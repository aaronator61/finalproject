# Generated by Django 4.1.2 on 2022-11-17 18:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CruiseLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CruiseLineName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_name', models.CharField(max_length=50)),
                ('cruise_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.cruiseline')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('start_date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('trip_length', models.IntegerField(default=0)),
                ('ship', models.ManyToManyField(blank=True, to='pages.ship')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=150)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.user')),
            ],
        ),
    ]
