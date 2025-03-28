from django.shortcuts import render, redirect, get_object_or_404
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Course.objects.create(name=name, description=description)
        return redirect('course_list')
    return render(request, 'course/add_course.html')

def update_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        course.name = request.POST['name']
        course.description = request.POST['description']
        course.save()
        return redirect('course_list')

    return render(request, 'course/update_course.html', {'course': course})

def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('course_list')
