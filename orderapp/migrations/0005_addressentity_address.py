# Generated by Django 2.2.4 on 2019-08-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0004_addressentity_ordermodels_orderprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressentity',
            name='address',
            field=models.CharField(default=1, max_length=200, verbose_name='用户地址'),
            preserve_default=False,
        ),
    ]