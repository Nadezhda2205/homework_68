from django.contrib import admin
from django.urls import path
from accounts.views import LoginView, logout_view, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', IndexView.as_view(), name='index'),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),


]
