# Generated by Django 4.1.3 on 2022-11-25 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_remove_resume_email_remove_resume_facebook_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='applicant',
        ),
        migrations.AddField(
            model_name='response',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
