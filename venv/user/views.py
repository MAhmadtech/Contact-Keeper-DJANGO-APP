from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisteration
from django.contrib import messages

def index(request):
    return render(request , 'main.html')

def register(request):
    if request.method == 'POST':
        reg_form = UserRegisteration(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('index')
        else:
            for field, errors in reg_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        reg_form = UserRegisteration()
    
    return render(request, 'register.html', {'reg_form': reg_form})

# def login(request):
#     return render(request, 'login.html')
# Create your views here.
