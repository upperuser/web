from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Student
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Студенты", 'url_name': 'students'},
        {'title': "Общежития", 'url_name': 'dormitory'},
        {'title': "Войти", 'url_name': 'login'}]

def index(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'students/index.html', context=context)

def about(request):
    return render(request, 'students/about.html', {'menu': menu, 'title': 'О сайте'})
def students(request):
    return HttpResponse("Студенты")
def dormitory(request):
    return HttpResponse("Общежития")
def login(request):
    return HttpResponse("Авторизация")


def show_student(request, stud_id):
    return HttpResponse(f"Отображение студента с id = {stud_id}")
def get_absolute_url(self):
    return reverse('student', kwargs={'stud_id': self.pk})