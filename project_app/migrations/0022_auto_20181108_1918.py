# Generated by Django 2.0.1 on 2018-11-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0021_auto_20181108_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatnode',
            name='created_date',
            field=models.CharField(default='2018-11-08 19:18:49', max_length=50),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='pdf',
            field=models.FileField(default='', upload_to=''),
        ),
    ]