# Generated by Django 4.1.3 on 2022-11-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_message_options_alter_response_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-11-14'),
            preserve_default=False,
        ),
    ]
