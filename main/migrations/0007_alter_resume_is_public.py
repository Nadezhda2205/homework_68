# Generated by Django 4.1.3 on 2022-11-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_response_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='is_public',
            field=models.BooleanField(blank=True),
        ),
    ]