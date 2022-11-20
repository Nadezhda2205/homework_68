from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import LoginView, logout_view, RegisterView, AccountDetailView, AccountUpdateView
from main.views import VacancyListView, VacancyCreateView, VacancyDetailView, \
    VacancyUpdateView, VacancyDateUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VacancyListView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<str:slug>', AccountDetailView.as_view(), name='account_detail'),

    path('<str:slug>/update', AccountUpdateView.as_view(), name='account_update'),

    path('vacancy/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/<int:pk>', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/<int:pk>/update', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy/<int:pk>/update_date', VacancyDateUpdateView, name='vacancy_date_update'),

    path('applicant/', include('main.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

