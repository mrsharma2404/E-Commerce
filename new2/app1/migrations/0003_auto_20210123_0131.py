# Generated by Django 3.1.4 on 2021-01-22 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210123_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product1',
            name='category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Product1',
        ),
    ]
