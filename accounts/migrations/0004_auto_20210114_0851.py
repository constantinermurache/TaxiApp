# Generated by Django 2.2 on 2021-01-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210114_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(default='Your Address', max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='county',
            field=models.CharField(default='Your County', max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='payment_method',
            field=models.CharField(default='Your Payment Method', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postcode',
            field=models.CharField(default='Your Postcode', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='town',
            field=models.CharField(default='Your Town', max_length=200),
        ),
        migrations.AlterField(
            model_name='driver',
            name='reg_No',
            field=models.CharField(default='Your Registration Plate', max_length=20),
        ),
    ]
