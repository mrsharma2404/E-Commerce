# Generated by Django 3.1.4 on 2021-01-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('offer_discount', models.IntegerField(default=0)),
                ('image2', models.ImageField(blank=True, null=True, upload_to='uploads/products/')),
                ('size', models.CharField(blank=True, default='free_size', max_length=200, null=True)),
                ('status', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
    ]
