from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def recepies(request):
    if request.method == "POST":

        data = request.POST
        recepie_name =data.get('recepie_name')
        recepie_image = request.FILES.get('recepie_image')
        recepie_discription = data.get('recepie_discription')
        
        Recepie.objects.create(
            recepie_name = recepie_name,
            recepie_discription= recepie_discription,
            recepie_image = recepie_image
            
        )
        return redirect('/recepies/')
    queryset= Recepie.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recepie_name__icontains = request.GET.get('search'))
        print(request.GET.get('search'))
    
   
    context = {'recepies': queryset}
    return render(request, 'recepies.html', context)
        
       


def delete_recepie(request, id):
    queryset = Recepie.objects.get(id = id)
    queryset.delete()
    print(id)
    return redirect('/recepies/')
def update_recepie(request, id):
    queryset = Recepie.objects.get(id = id)
    if request.method == "POST":
         data = request.POST
         recepie_name =data.get('recepie_name')
         recepie_image = request.FILES.get('recepie_image')
         recepie_discription = data.get('recepie_discription')

         queryset.recepie_name = recepie_name
         queryset.recepie_discription = recepie_discription

         if recepie_image:
              queryset.recepie_image= recepie_image
         queryset.save()
         return redirect('/recepies/')




        

    print(queryset)
    context= {'recepie': queryset}
    return render(request,'update_recepies.html',context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("user",username)
        
        print(User.objects.values_list('username', flat=True))
        if not User.objects.filter(username = username).exists():
            print("hiiiiiiiiii",username)
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recepies/')


    return render(request, "login.html")
def logout_page(request):
    logout(request)

    return redirect('/login/')




def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request,'Username already exist')
            return redirect('/register/')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()

        messages.info(request, 'Account successfully created')

        return redirect('/register/')
    return render(request, 'register.html')


















































