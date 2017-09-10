from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.template import RequestContext
from django.template.loader import get_template

from myformtest import models
from myformtest.ContactForm import ContactForm
from myformtest.StudentForm import StudentForm
from myformtest.models import Student


def login(request):
    try:
        userid = request.GET['user_id']
        pwd = request.GET['pwd']
    except:
        userid = None

    if userid != None and pwd == '12345':
        verified = True
    else:
        verified = False
    template = get_template('login.html')
    html = template.render(locals())
    return HttpResponse(html)


def contact(request):
    form = ContactForm()
    template = get_template('contact.html')
    """    why?
        request_context = RequestContext(request)
        request_context.push(locals())
        html = template.render(request_context)
    """
    html = template.render(locals())

    return HttpResponse(html)


def studentmsg(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            stu = Student(name=name, gender=gender, age=20)
            stu.save()
            isSave = True
        else:
            isSave = False
    else :
        form = StudentForm(request.GET)
        if form.is_valid():
            name = request.GET.get('name')
            gender = request.GET.get('gender')
            stu = Student(name=name, gender=gender, age=20)
            stu.save()
            isSave = True
        else:
            isSave = False
    return render(request, 'studentinfo.html', locals())
