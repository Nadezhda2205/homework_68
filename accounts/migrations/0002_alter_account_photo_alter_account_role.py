# Generated by Django 4.1.3 on 2022-11-12 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='accounts.role', verbose_name='Роль'),
        ),
    ]
