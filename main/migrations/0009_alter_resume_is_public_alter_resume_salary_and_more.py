# Generated by Django 4.1.3 on 2022-11-19 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_resume_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='is_public',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Желаемая зарплата'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='vacancy_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='main.vacancycategory', verbose_name='Категория вакансии'),
        ),
    ]
