from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    peoples = [
        {'name':'keerthika','age':23},
        {'name':'sharath','age':29},
        {'name':'vanshi','age':10},
        {'name':'Golu','age':4},
        {'name':'seetha','age':55},
    ]
    for people in peoples :
        if people['age'] :
            print("Yes")

 #   text = """
  #  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
   # """

    vegetables = ['Pumpkin','Tomato','potato']

    
    return render(request,"home/index.html",context = {'page': 'Django 2023 Tutorial','peoples':peoples, 
                                                       #'text':text
                                                       'vegetables':vegetables
                                                       })

def about(request):
    context = { 'page': 'About'}

    return render(request, "home/about.html",context)

def contact(request):
    context = {'page':'Contact'}
    return render(request, "home/contact.html",context)


    return render(request,"home/contact.html",context)
def success_page(request):
    print("*"*10)
    return HttpResponse("""<h1>This is a SUCCESS page<h1>""")

