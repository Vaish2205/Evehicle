# Generated by Django 4.2 on 2024-03-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0012_bookslots_accountno_bookslots_hname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deletedbooking',
            name='accountno',
            field=models.CharField(default='0', max_length=120),
        ),
        migrations.AddField(
            model_name='deletedbooking',
            name='hname',
            field=models.CharField(default='0', max_length=120),
        ),
        migrations.AddField(
            model_name='deletedbooking',
            name='ifsccode',
            field=models.CharField(default='0', max_length=120),
        ),
        migrations.AddField(
            model_name='deletedbooking',
            name='total',
            field=models.CharField(default='0', max_length=120),
        ),
    ]
