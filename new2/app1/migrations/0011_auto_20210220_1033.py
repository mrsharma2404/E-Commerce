# Generated by Django 3.1.4 on 2021-02-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_cart_price2'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
