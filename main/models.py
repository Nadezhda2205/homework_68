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
        on_delete=models.CASCADE
    )
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField()


    def __str__(self) -> str:
        return f'{self.author}: {self.vacancy_category}'
    
    class Meta():
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


class Experience(models.Model):
    begin_at = models.DateField()
    end_at = models.DateField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    duties = models.TextField(verbose_name='Обязанности')
    resume = models.ForeignKey(
        Resume, 
        verbose_name=('Резюме'), 
        on_delete=models.CASCADE, 
        related_name='experiences' 
    )
    
    def __str__(self) -> str:
        return f'{self.resume.author}: {self.company}: {self.position}'
    
    class Meta():
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class Education(models.Model):
    begin_at = models.DateField()
    end_at = models.DateField()
    description = models.TextField()
    resume = models.ForeignKey(
        Resume, 
        verbose_name=('Резюме'), 
        on_delete=models.CASCADE, 
        related_name='educations' 
    )
    
    def __str__(self) -> str:
        return f'{self.resume.author}: Период обучения с {self.begin_at} по {self.end_at}'
    
    class Meta():
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'



class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(verbose_name='Зарплата', null=True)
    description = models.TextField(null=True)
    experience_time = models.PositiveIntegerField(null=True, verbose_name='Опыт работы(лет)')
    vacancy_category = models.ForeignKey(
        'main.VacancyCategory', 
        verbose_name=('Категория вакансии'), 
        on_delete=models.CASCADE, 
        related_name='vacancies' 
    )
    is_public = models.BooleanField()
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(), 
        related_name='vacancies', 
        on_delete=models.CASCADE
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta():
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-updated_at']


class Response(models.Model):
    vacancy = models.ForeignKey(
        'main.Vacancy', 
        verbose_name=('Вакансия'), 
        on_delete=models.CASCADE, 
        related_name='responses' 
    )
    applicant = models.ForeignKey(
        'accounts.Account', 
        verbose_name=('Соискатель'), 
        on_delete=models.CASCADE, 
        related_name='responses' 
    )
    resume = models.ForeignKey(
        'main.Resume', 
        verbose_name=('Резюме'), 
        on_delete=models.CASCADE, 
        related_name='responses' 
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Отклик на {self.vacancy}'
    
    class Meta():
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'


    
class Message(models.Model):
    response = models.ForeignKey(
        'main.Response', 
        verbose_name=('На отклик'), 
        on_delete=models.CASCADE, 
        related_name='messages' 
    )
    author = models.ForeignKey(
        to=get_user_model(), 
        verbose_name='Автор',
        related_name='messages', 
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.author}: {self.created_at}'
    
    class Meta():
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


