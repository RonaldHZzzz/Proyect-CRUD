
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect # redireccionar 
from django.contrib.auth import authenticate #funcion para autenticar a los usuarios

def index(request):
    return render(request,'index.html',{
        'message':'listado de productos',
        'products':[
            {'title':'playera','price':5,'stock':True},#producto
            {'title':'pantalon','price':10,'stock':True},
            {'title':'mochila','price':20,'stock':False},
            {'title':'reloj','price':500,'stock':True},
            {'title':'rodillera','price':4,'stock':False},
             {'title':'zapato','price':400,'stock':True},
                
                
        ]
        
    })

def login_view(request):
    if request.method== 'POST':
        USERNAME = request.POST.get('username')
        PASSWORD = request.POST.get('password')
        user = authenticate(username=USERNAME,password=PASSWORD)
        if user:
           login(request,user)
           return redirect('index')
    return render(request,"users/login.html",{

    })