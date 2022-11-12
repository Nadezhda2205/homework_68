from django.db import models
from django.contrib.auth import get_user_model


class VacancyCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta():
        verbose_name = 'Категория вакансии'
        verbose_name_plural = 'Категории вакансий'


class Resume(models.Model):
    vacancy_category = models.ForeignKey(
        'main.VacancyCategory', 
        verbose_name=('Категория вакансии'), 
        on_delete=models.CASCADE, 
        related_name='resumes' 
    )
    salary = models.PositiveIntegerField(verbose_name='Желаемая зарплата', null=True)
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(), 
        related_name='resumes', 
        null=False, 
        blank=False,
        on_delete=models.CASCADE
    )
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField()


    def __str__(self) -> str:
        return f'{self.author}: {self.vacancy_category}'
    
    class Meta():
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


