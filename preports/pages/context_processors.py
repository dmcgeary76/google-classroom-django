from .models import Courses

def add_variable_to_context(request):
    try:
        courses = Courses.objects.filter(name__contains='Getting Good').values('shortname')
    except:
        print('Encountered a problem in creating course list.')
        courses = []
    context = {
        'courses': courses,
    }
    return context
