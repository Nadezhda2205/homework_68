from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import LoginView, logout_view, IndexView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', IndexView.as_view(), name='index'),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('register/', RegisterView.as_view(), name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
