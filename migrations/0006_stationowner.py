# Generated by Django 4.2 on 2023-09-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_payment_remove_bookslots_accountno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stationowner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=80)),
                ('fname', models.CharField(max_length=89)),
                ('lname', models.CharField(max_length=88)),
                ('email', models.EmailField(max_length=90)),
                ('pass1', models.CharField(max_length=90)),
                ('pass2', models.CharField(max_length=90)),
            ],
        ),
    ]
