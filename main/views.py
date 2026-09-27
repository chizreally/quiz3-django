from django.shortcuts import render
from main.models import Student

def home(request):
    return render(request, 'main/home.html')

def show_students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students.html', context)