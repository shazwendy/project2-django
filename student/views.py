from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import redirect

from .forms import StudentForm
from .models import Student

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("list_students")
            return HttpResponse("valid data",status = 200)

        else:
            return HttpResponse("invalid data",status = 400)

    else:
        form = Student()
        return  render(request,"add_student.html",{"form":form})

def list_students(request):
        students = Student.objects.all()
        return render (request, "all_students.html", {"students":students})

def student_details(request,pk):
        student = Student.objects.get(pk = pk)
        return render(request,"student_details.html", {"student":student})


def edit_student(request,pk):
        student = Student.objects.get(pk = pk)
        if request.method == "POST":
            form = StudentForm(request.POST,instance = student)
            if form.is_valid:
                form.save()
                return redirect("list_students")

        else:
            form = StudentForm(instance = student)
            return render(request, "edit_student.html",{"form":form})


# Create your views here.
