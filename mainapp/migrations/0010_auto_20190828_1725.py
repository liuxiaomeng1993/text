# Generated by Django 2.2.4 on 2019-08-28 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_cartentity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartentity',
            name='no',
            field=models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='购物车编号'),
        ),
        migrations.CreateModel(
            name='FtuitCartEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt', models.IntegerField(default=1, verbose_name='数量')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.CartEntity', verbose_name='购物车编号')),
                ('fruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.FruitEntity', verbose_name='水果')),
            ],
            options={
                'verbose_name': '购物车详情表',
                'verbose_name_plural': '购物车详情表',
                'db_table': 't_fruit_cart',
            },
        ),
    ]
