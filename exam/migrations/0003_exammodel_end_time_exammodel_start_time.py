# Generated by Django 5.1.7 on 2025-03-31 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_exammodel_date_exammodel_status_exammodel_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammodel',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exammodel',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
