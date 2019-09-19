# Generated by Django 2.2.4 on 2019-08-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20190827_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeentity',
            name='logo',
            field=models.ImageField(blank=True, height_field='logo_height', null=True, upload_to='store', verbose_name='LOGO', width_field='logo_width'),
        ),
        migrations.AddField(
            model_name='storeentity',
            name='logo_height',
            field=models.IntegerField(null=True, verbose_name='LOGO高'),
        ),
        migrations.AddField(
            model_name='storeentity',
            name='logo_width',
            field=models.IntegerField(null=True, verbose_name='LOGO宽'),
        ),
        migrations.AddField(
            model_name='storeentity',
            name='opened',
            field=models.BooleanField(default=False, verbose_name='是否开业'),
        ),
        migrations.AddField(
            model_name='storeentity',
            name='summary',
            field=models.TextField(blank=True, null=True, verbose_name='介绍'),
        ),
        migrations.AlterField(
            model_name='storeentity',
            name='store_type',
            field=models.CharField(choices=[('1', '自营'), ('2', '第三方')], db_column='type_', max_length=10, verbose_name='类型'),
        ),
    ]
