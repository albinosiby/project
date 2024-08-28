from django.shortcuts import render, redirect # type: ignore
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll_number = request.POST['roll_number']
        age = request.POST['age']
        email = request.POST['email']
        student = Student(name=name, roll_number=roll_number, age=age, email=email)
        student.save()
        return redirect('home')  # Redirect back to the home page
    return render(request,'add_student.html')

def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('home')