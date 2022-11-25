from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import LoginView, logout_view, RegisterView, AccountDetailView, AccountUpdateView

from main.views import (
    VacancyListView,
    VacancyCreateView,
    VacancyDetailView,
    VacancyUpdateView,
    get_messages_view,
    vacancy_date_update_view,
    MessageCreateView,
    ResponseCreateView
)

from main.view import json_index


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
    path('vacancy/<int:pk>/update_date', vacancy_date_update_view, name='vacancy_date_update'),
    path('response/create/', ResponseCreateView.as_view(), name='response_create'),

    path('applicant/', include('main.urls')),

    path('response/<int:pk>/message/create/', MessageCreateView.as_view(), name='message_create'),
    path('response/<int:pk>/messages/', get_messages_view, name='messages_list'),
    path('json-index/',json_index, name='json_index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
