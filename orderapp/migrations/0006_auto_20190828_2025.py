# Generated by Django 2.2.4 on 2019-08-28 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0005_addressentity_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderprofile',
            name='num',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderapp.OrderModels', verbose_name='订单号'),
        ),
    ]
