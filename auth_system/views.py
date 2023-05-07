from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from myapp.models import Image
from myapp.forms import ImageForm

@login_required
def HomePage(request):
    form = ImageForm()
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('home-page')

    images = Image.objects.filter(user=request.user)
    return render(request, 'auth_system/index.html', {'form': form, 'images': images})


def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')

    return render(request, 'auth_system/register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request, 'auth_system/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login-page')

def test(request):
    return render(request, 'auth_system/test.html', {})


def delete_image(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image = Image.objects.get(id=image_id)

        # Check if the user is authenticated and the image belongs to the user
        if request.user.is_authenticated and request.user == image.user:
            # Delete the image from the database and the file system
            image.delete()

    return redirect('home-page')
