# Generated by Django 3.0.6 on 2020-07-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.CharField(default='', max_length=20),
        ),
    ]
