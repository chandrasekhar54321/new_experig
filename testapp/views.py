from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from testapp.models import student_register
from django.contrib import messages
# Create your views here.
def index(request):
	return render(request,'index.html')
def student_signups(request):
	if request.method=="POST":
		username=request.POST.get("username")
		first_name=request.POST.get("first_name")
		last_name=request.POST.get("last_name")
		email=request.POST.get("email")
		location=request.POST.get("location")
		password=request.POST.get("password")
		cnf_password=request.POST.get("cnf_password")
		if User.objects.filter(username=username).exists():
			messages.info(request,'Username Taken')
			return redirect('/student_signups')
		elif User.objects.filter(email=email).exists():
			messages.info(request,'Email Id Taken') 
			return redirect('/student_signups')
		elif password != cnf_password:
			messages.info(request,'Confirm Password not Match') 
			return redirect('/student_signups')
		else:
			user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
			user.save()
			user_id=user.id
			type_of_user="STUDENT"
			data=student_register(user_id=user_id,location=location,type_of_user=type_of_user)
			data.save()
			messages.success(request,"Data Save Successfully")
			return redirect('/student_signups')
	else:
		return render(request,'student_signup.html')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/student_dashboard')
        else:
            messages.info(request,'Invalid credential')  
            return redirect('/login')  
    else:
        return render(request,'student_signup.html')
def logout(request):
    auth.logout(request)
    return redirect('/student_signups')
def student_dashboard(request):
	return render(request,'student_dashboard.html')
def student_profile(request):
	return render(request,'student_profile.html')