from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import LoginView, logout_view, RegisterView, AccountDetailView
from main.views import VacancyListView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', VacancyListView.as_view(), name='index'),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('register/', RegisterView.as_view(), name='register'),

    path('<str:slug>', AccountDetailView.as_view(), name='account_detail')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
