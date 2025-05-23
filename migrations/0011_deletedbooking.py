# Generated by Django 4.2 on 2024-03-20 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0010_bookslots_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oname', models.CharField(max_length=100)),
                ('vehicleno', models.CharField(max_length=20)),
                ('mobileno', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('deletion_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
