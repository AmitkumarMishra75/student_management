from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse

details = Student.objects.all()

def name(request):
    context = {
        'students' : details
    }
    return  render(request,'index.html',context)

def py(request):
    context = {
        'students' : details
    }
    return  render(request,'PY.html',context)

def j(request):
    context = {
        'students' : details
    }
    return  render(request,'J.html',context)

def q(request):
    context = {
        'students' : details
    }
    return  render(request,'Q.html',context)

def pro(request):
    context = {
        'students' : details
    }
    return  render(request,'PRO.html',context)

def display(request,pk):
    try:
        data1 = Student.objects.get(id = pk)
    except Student.DoesNotExist:
        return HttpResponse("Student data not present")
        
    if request.method == "POST":
        data1.delete()
        return redirect('name')
    context = {
        'data1':data1
    }
    return render(request,'display.html',context)

def edit(request,ab):
    edit = True
    data2 = Student.objects.get(id = ab)
    if request.method == "POST":
        NAME = request.POST.get('NAME')
        QUALIFICATION = request.POST.get('QUALIFICATION')
        GENDER = request.POST.get('GENDER')
        YOP = request.POST.get('YOP')
        AGE = request.POST.get('AGE')
        SKILLS = request.POST.get('SKILLS')
        DOB = request.POST.get('DOB')
        ADDRESS = request.POST.get('ADDRESS')
        MOCK_RATING = request.POST.get('MOCK_RATING')
        DEPARTMENT = request.POST.get('DEPARTMENT')
        print(NAME,QUALIFICATION,GENDER,YOP,AGE,SKILLS,DOB,ADDRESS,MOCK_RATING,DEPARTMENT)
        data2.NAME = NAME
        data2.QUALIFICATION = QUALIFICATION
        data2.GENDER = GENDER
        data2.YOP = YOP
        data2.AGE = AGE
        data2.SKILLS = SKILLS
        # data2.DOB = DOB
        data2.ADDRESS = ADDRESS
        data2.MOCK_RATING = MOCK_RATING
        data2.DEPARTMENT = DEPARTMENT
        data2.save()
        print(NAME,QUALIFICATION,GENDER,YOP,AGE,SKILLS,DOB,ADDRESS,MOCK_RATING,DEPARTMENT)
    context = {
        'data2':data2
    }
    return render(request,'edit.html',context)

def create(request):
    edit = False
    if request.method == "POST":
        NAME = request.POST.get('NAME')
        QUALIFICATION = request.POST.get('QUALIFICATION')
        GENDER = request.POST.get('GENDER')
        YOP = request.POST.get('YOP')
        AGE = request.POST.get('AGE')
        SKILLS = request.POST.get('SKILLS')
        DOB = request.POST.get('DOB')
        ADDRESS = request.POST.get('ADDRESS')
        MOCK_RATING = request.POST.get('MOCK_RATING')
        DEPARTMENT = request.POST.get('DEPARTMENT')
        a = Student.objects.create(NAME = NAME, QUALIFICATION = QUALIFICATION, GENDER = GENDER, YOP = YOP, AGE = AGE, SKILLS = SKILLS, DOB = DOB, ADDRESS = ADDRESS, MOCK_RATING = MOCK_RATING, DEPARTMENT = DEPARTMENT)
        return redirect("name")
    return render(request,'add.html',{'edit':edit})