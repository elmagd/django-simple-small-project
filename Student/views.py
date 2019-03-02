from django.shortcuts import render
from django.http import HttpResponse
from Student.student import Student


def index(request):
    students = [Student(1, "Hadeel"),
                Student(2, "Aya"),
                Student(3, "Walid")]
    return render(request, "Student/index.html", {"allStudents": students})


def details(request, student_id):
    student = Student(student_id, "XXX")
    return render(request, "Student/details.html", {"student":student})