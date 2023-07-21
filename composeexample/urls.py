
from django.contrib import admin
from django.urls import path
from my_app import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  
    path('accounts/signup/', views.signup, name='signup'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login')
]