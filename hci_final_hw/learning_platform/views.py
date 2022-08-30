from django.shortcuts import render, redirect
from .models import *
from .forms import PlatformUserForm

# Create your views here.

def courses(request):
    queryset = Course.objects.all()
    context = {'courses': queryset}
    return render(request, 'courses.html', context = context)

def course_info(request, course_title):
    queryset = Course.objects.filter(title = course_title).all()
    context = {'courses': queryset}
    return render(request, 'course_info.html',  context = context)

def course_page(request, course_title):
    queryset = Course.objects.filter(title = course_title).all()
    context = {'courses': queryset}
    return render(request, 'course_page.html', context = context)

def index(request):
    if request.method == 'POST':
        form_data = PlatformUserForm(request.POST)
        if form_data.is_valid():
            platform_user = form_data.save(commit = False)
            platform_user.user = request.user
            platform_user.save()
            return redirect('/index/')
    context = {'form': PlatformUserForm}
    return render(request, 'index.html', context = context)

def account(request):
    queryset = PlatformUser.objects.filter(user = request.user).all()
    context = {'users': queryset}
    return render(request, 'account.html', context = context)

def about(request):
    return render(request, 'about.html')