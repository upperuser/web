from django.urls import path
from .views import index, dormitory, about, login, show_student, students

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('students/', students, name='students'),
    path('dormitory/', dormitory, name='dormitory'),
    path('login/', login, name='login'),
    path('student/<int:stud_id>/', show_student, name='student'),
]