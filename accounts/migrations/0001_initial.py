# Generated by Django 2.2 on 2021-01-04 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('town', models.CharField(max_length=200, null=True)),
                ('county', models.CharField(max_length=200, null=True)),
                ('postcode', models.CharField(max_length=20, null=True)),
                ('payment_method', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('reg_No', models.CharField(max_length=20, null=True)),
                ('availability', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_booked', models.DateTimeField(auto_now_add=True, null=True)),
                ('start_address', models.CharField(max_length=200, null=True)),
                ('destination_address', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(null=True, verbose_name='Trip Date')),
                ('time', models.TimeField(null=True, verbose_name='Trip Time')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Finished', 'Finished')], max_length=15, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Driver')),
            ],
        ),
    ]
