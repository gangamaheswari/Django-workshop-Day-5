from django.shortcuts import render,redirect
from django.http import HttpResponse
from CrudAPP.models import student
# Create your views here.
def insert(request):
	if request.method=="POST":
		name=request.POST['uname']
		roll=request.POST['rollnum']
		ag=request.POST['age']
		mobile=request.POST['mobilenum']
		em=request.POST['email']
		add=request.POST['address']
		student.objects.create(name=name,rollnum=roll,age=ag,mobile=mobile,email=em,address=add)
		return redirect('/read')
	return render(request,'insert.html',{})

def read(request):
	data=student.objects.all()
	return render(request,'read.html',{'info':data})
def update(request,id):
	data=student.objects.get(id=id)
	return render(request,'update.html',{'data':data})

        
        

        

       

	