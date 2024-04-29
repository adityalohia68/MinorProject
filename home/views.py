from django.shortcuts import render, redirect
from home.models import BookAppointment
from datetime import datetime
from django.contrib.auth import authenticate, logout, login

# Create your views here.



def bookPage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('emaol')
        phone = request.POST.get('phone')
        state = request.POST.get('state')

        bookappointment = BookAppointment(name=name, age=age, email=email, phone=phone, state=state, date=datetime.now())
        bookappointment.save()

    return render(request, 'book.html')





def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'homePage.html')
    
    
    

def loginUser(request):
    if request.method == 'POST':
        # check if the credentials are correct or not
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')





def manage(request):
    print("--------------------------------------------", request.user)
    if request.doctor.is_anonymous:
        return redirect('/docLogin')
    else:
        return render(request, 'manage.html')





def docLogin(request):
    if request.method == 'POST':
        # check if the credentials are correct or not
        docname = request.POST.get("docname")
        docpassword = request.POST.get("docpassword")

        doctor = authenticate(docname=docname, docpassword=docpassword)
        
        if doctor is not None:
            login(request, doctor)
            return redirect('/manage')
        else:
            return render(request, 'docLogin.html')
    return render(request, 'docLogin.html')




    
def register(request):
    return render(request, 'register.html')

def docRegis(request):
    return render(request, 'docRegis.html')