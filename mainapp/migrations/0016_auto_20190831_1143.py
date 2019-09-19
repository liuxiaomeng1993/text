# Generated by Django 2.2.4 on 2019-08-31 03:43

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20190829_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentity',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[mainapp.models.UserValidator.valid_phone], verbose_name='手机号'),
        ),
    ]