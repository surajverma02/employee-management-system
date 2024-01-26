"""
Views configuration with Urls for myapp project.

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(request):
    print("Index Page Is Called !")
    # return HttpResponse("<h1>Welcome to the world of Programming</h1>")
    return render(request, "home.html", {})
    # return render(request, "emp/home.html", {})

def about(request):
    print("About Page Is Called !")
    dateToday = datetime.datetime.now()
    name = "Suraj"
    # isActive = True
    marks = [9, 8, 7, 8, 10]
    student = {
        'studentName' : "Suraj",
        'studentCollege': 'ARSD College',
        'studentCity': 'Uttar Pradesh'
    }
    # return HttpResponse("<h1>Here is something about me</h1>")

    data = {
        'date' : dateToday,
        # 'isActive' : isActive,
        'name' : name,
        'marks' : marks,
        'studentData': student
    }
    return render(request, "about.html", data)

def services(request):
    print("Services Page Is Called !")
    # return HttpResponse("<h1>Now I am telling what can i do</h1>")
    return render(request, "services.html", {})

def contact(request):
    isActive = True
    # Taking data from the web page / user
    if request.method == 'POST': 
        check = request.POST.get('check')
        print(check)
        if check == None:
            isActive = False
        else:
            isActive = True

    print("Contact Page Is Called !")
    # return HttpResponse("<h1>Contact me</h1>")
    return render(request, "contact.html", {'isActive':isActive})