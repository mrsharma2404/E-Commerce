# Generated by Django 3.1.4 on 2021-02-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_auto_20210221_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Trending',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
