# Generated by Django 3.2.8 on 2021-10-06 19:01

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_response_insult_comeback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insult',
            name='insult',
            field=app.models.LowerCaseField(max_length=200),
        ),
    ]