from unicodedata import category
from django.contrib import messages
from django.shortcuts import render,redirect
from . models import Book
from django.contrib.auth.models import User
from django.contrib import auth

def Library(request):
    data=Book.objects.all()
    return render(request,'index.html',{'showbook':data})

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        rpassword=request.POST['rpassword']
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username already exists')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'E-mail already exists')
            return redirect('/signup')
        elif password!=rpassword:
            messages.error(request,'Password did not match')
            return redirect('/signup')
        else:
            user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
            user.save()
            return redirect('/')
    else:
        return render(request,'signup.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'Invalid Username or Password')
            return redirect('/login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    messages.warning(request,'Sucessfully Logout')
    return redirect('/')

def addbook(request):
    if request.method=='POST':
        b=Book()
        b.BookName=request.POST['bname']
        b.Author=request.POST['author']
        b.Category=request.POST['category']
        b.save()
        messages.success(request,'Book Added Successfully')
        return redirect('/')
    else:
        return render(request,'addbook.html')
    
def showbook(request):
    data=Book.objects.all()
    return render(request,'showbook.html',{'showbook':data})

def delete(request):
    id=request.GET['id']
    Book.objects.filter(id=id).delete()
    data=Book.objects.all()
    return render(request,'showbook.html',{'showbook':data})

def update(request):
    b=Book()
    b.id=request.POST['id']
    b.BookName=request.POST['bname']
    b.Author=request.POST['author']
    b.Category=request.POST['category']
    b.save()
    data=Book.objects.all()
    return render(request,'showbook.html',{'showbook':data})



        