# Generated by Django 5.1.1 on 2024-09-28 11:26

import drugs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=drugs.models.upload_to),
        ),
    ]
