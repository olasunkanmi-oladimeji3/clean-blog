# Generated by Django 2.2 on 2021-01-12 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contactforms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactforms',
            name='Phone_Number',
            field=models.PositiveIntegerField(max_length=11),
        ),
    ]
