# Generated by Django 2.0.1 on 2018-11-03 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_auto_20181103_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 3, 20, 43, 59, 69600)),
        ),
    ]