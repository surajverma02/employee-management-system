from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Emp, Testimonials

# Create your views here.
def empHome(request):
    emps = Emp.objects.all()
    return render(request, "emp/home.html", {'emp':emps})

def addEmp(request):
    if request.method=="POST":
        
        # Data fetch
        empName  = request.POST.get("empname")
        empId  = request.POST.get("empid")
        empPhone  = request.POST.get("empphone")
        empAddress  = request.POST.get("empaddress")
        empWorking  = request.POST.get("empworking")
        empDepartment  = request.POST.get("empdepartment")

        # create models object and set data
        e = Emp()
        e.name = empName
        e.empId = empId
        e.phone = empPhone
        e.address = empAddress
        e.department = empDepartment

        if empWorking is None:
            e.working = False
        else:
            e.working = True
        e.save()

        # save the objects

        #prepare message


        return redirect('/emp/home/')
    return render(request, "emp/addEmp.html", {})

def delEmp(request, empid):
    emp = Emp.objects.get(id=empid)
    emp.delete()
    return redirect('/emp/home/')

def updateEmp(request, empid):
    emp = Emp.objects.get(id=empid)
    return render(request, "emp/updateEmp.html", {'emp':emp})

def updated(request, empid):
    
    if request.method=="POST":
        
        # Data fetch
        empName  = request.POST.get("empname")
        empId  = request.POST.get("empid")
        empPhone  = request.POST.get("empphone")
        empAddress  = request.POST.get("empaddress")
        empWorking  = request.POST.get("empworking")
        empDepartment  = request.POST.get("empdepartment")

        # create models object and set data
        e = Emp.objects.get(id=empid)
        e.name = empName
        e.empId = empId
        e.phone = empPhone
        e.address = empAddress
        e.department = empDepartment

        if empWorking is None:
            e.working = False
        else:
            e.working = True
        e.save()    

    return redirect('/emp/home/')


def Testimonial(request):
    test = Testimonials.objects.all()
    return render (request, "emp/testimonial.html", {'test':test})