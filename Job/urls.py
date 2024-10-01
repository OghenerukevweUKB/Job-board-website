from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.JobList, name='job_list'),
    path('register', views.Register, name='register'),
    path('<int:job_id>/apply/', views.ApplyForJob, name='apply_for_job'),
    path('login', auth_views.LoginView.as_view(template_name='job/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='job/logout.html'), name='logout')
]
