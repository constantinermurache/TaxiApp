# Generated by Django 2.2 on 2021-01-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210113_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='Your Phone', max_length=20),
        ),
    ]