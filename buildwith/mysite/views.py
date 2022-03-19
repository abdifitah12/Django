from django.shortcuts import render
from .models import Person,Course,Lesson, Section

# Create your views here.


def index(request):
    return render(request, "test.html")

#def Course(request):
     #allcourses = Course.objects.all()
     #return render(request, "Course.html", {'Course':'allcourses'}) 
def Courser(request):
    position = Course.objects.all()
    context = {'job': position}

    response = render(request, 'Course.html', context)
    return response      


    
def blog(request):
    return render(request, "blog.html")


def pricing(request, num):
    course = Course.objects.get(id=num)
    #QuerySet
    lessons = Lesson.objects.filter(course=course)
    sections = Section.objects.filter(course=course)
    
    context = {
        'numbers': num,
        'courses_obj': course,
        'lessons': lessons,
        'sections': sections
         
           }
    return render(request, "pricing.html",context)



#this  comment testing commit

def optin(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        email = request.POST.get('email')

        info = Person(name=name, country=country, email=email)
        info.save()
        opt = True
        context = {'optedin': opt}
        return render(request, 'optin.html', context)

    else:
        return render(request, 'optin.html')

