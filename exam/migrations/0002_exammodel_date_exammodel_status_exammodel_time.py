# Generated by Django 5.1.7 on 2025-03-31 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammodel',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exammodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='exammodel',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
