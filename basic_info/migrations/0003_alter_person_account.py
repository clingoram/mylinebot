# Generated by Django 5.0.1 on 2024-05-03 07:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0002_message_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='account',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(code='invalid_Account', message='Account must be Alphanumeric', regex='^[a-zA-Z0-9]*$')]),
        ),
    ]
