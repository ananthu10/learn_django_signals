# Generated by Django 3.2.5 on 2021-07-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total', models.IntegerField(blank=True)),
                ('total_price', models.PositiveIntegerField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('cars', models.ManyToManyField(to='cars.Car')),
            ],
        ),
    ]
