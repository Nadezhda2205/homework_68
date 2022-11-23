# Generated by Django 4.1.3 on 2022-11-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_resume_email_resume_facebook_resume_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(default='null', max_length=254, verbose_name='Почта email'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='facebook',
            field=models.CharField(blank=True, default='null', max_length=100, verbose_name='Ссылка на facebook'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='linkedin',
            field=models.CharField(blank=True, default='null', max_length=100, null=True, verbose_name='Ссылка на linkedIn'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(default='null', max_length=100, verbose_name='Название резюме'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(default='null', max_length=30, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='telegram',
            field=models.CharField(default='null', max_length=100, verbose_name='Телеграм'),
        ),
    ]