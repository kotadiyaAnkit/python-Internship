from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving

from .views import home, login_page,register_view




from django.urls import path
from . import views



urlpatterns = [
    path('home/',views.home, name="home"),
    path('about/', views.about, name='about'),
    path("contact/", views.contact, name="contact"),
    path("admin/", admin.site.urls),          # Admin interface
    path("student/", views.student_register, name='student'),
    
    path('students/', views.student_register, name='student_list'),
    path('show/', views.student_list, name='show'), 
    path('student/update/<int:pk>/', views.student_update, name='student_update'),
    path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),

     path('logout/', views.logout_view, name='logout'),

    path('login/', login_page, name='login_page'),    # Login page
    path('register/', register_view, name='register'),
    
    
   
]