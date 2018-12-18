from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import Courses, Assignments, Enrollments, Students, Grades

# Create your views here.


def page_view(request, *args, **kwargs):
    return render(request, "page.html", {})


def login_view(request, *args, **kwargs):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html', {})


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def logout(request):
    auth_logout(request)
    return redirect('/')


def investigating_view(request, *args, **kwargs):
    grade_matrix = get_grades('Investigating')
    assignments = get_assignments('Investigating')
    context = {
        'grade_matrix': grade_matrix,
        'assignments':  assignments,
    }
    return render(request, 'investigating.html', context)


def get_grades (shortname):
    # Get the course_id for the target course
    try:
        course_id = Courses.objects.filter(shortname__exact=shortname).values('id')[0]['id']
    except:
        print('There was an error in retrieving the course_id for ' + shortname + '.')

    # Get the assignment list for the corresponing course
    try:
        assignments = Assignments.objects.filter(courseid__exact = courseid).values()
    except:
        print('There was an error in retrieving the assignment list for ' + shortname + '.')

    # Get the enrollment records for the retrieved course_id
    try:
        enrollments = Enrollments.objects.filter(courseid__exact=course_id).values('studentid')
    except:
        print('There was an error retrieving the enrollments for ' + shortname + '.')

    # Get student names and the grade data for each assignments


def get_assignments(shortname):
    # Get the course_id for the target course
    try:
        course_id = Courses.objects.filter(shortname__exact=shortname).values('id')[0]['id']
    except:
        print('There was an error in retrieving the course_id for ' + shortname + '.')

    # Get the assignment list for the corresponing course
    try:
        assignments = Assignments.objects.filter(courseid__exact = courseid).values()
    except:
        print('There was an error in retrieving the assignment list for ' + shortname + '.')

    return assignments
