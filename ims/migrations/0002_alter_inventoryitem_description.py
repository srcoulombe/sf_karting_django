# Generated by Django 3.2.11 on 2022-01-18 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
