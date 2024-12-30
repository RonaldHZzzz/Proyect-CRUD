from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html',{
        'message':'listado de productos',
        'products':[
            {'title':'playera','price':5,'stock':True},#producto
            {'title':'pantalon','price':10,'stock':True},
            {'title':'mochila','price':20,'stock':False},
            {'title':'reloj','price':500,'stock':True},
            {'title':'rodillera','price':4,'stock':False},
            
        ]
        
    })

def login(request):
    if request.method== 'POST':
        USERNAME = request.POST.get('username')
        PASSWORD = request.POST.get('password')
        print(USERNAME)
        print(PASSWORD)
    return render(request,"users/login.html",{

    })