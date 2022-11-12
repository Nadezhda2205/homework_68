from django.contrib import admin
from main.models import VacancyCategory, Resume, Education, Experience, Vacancy


'''Декоратор регистрирует в админ панели модель'''
@admin.register(VacancyCategory)
class VacancyCategoryAdmin(admin.ModelAdmin):
    '''Лист дисплэй выводит все поля из модели'''
    list_display = [field.name for field in VacancyCategory._meta.fields]


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Resume._meta.fields]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Education._meta.fields]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Experience._meta.fields]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vacancy._meta.fields]

