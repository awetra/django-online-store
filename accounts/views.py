from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('all_products_list')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email):
            pass
    return render(request, 'accounts/register.html')