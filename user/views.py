from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import CustomUser, PersonInfo
from .forms import LoginForm
from main.models import BetHistory

@login_required
def profile(request):
    user_profile = PersonInfo.objects.get(user=request.user.pk)
    context = {'user_profile': user_profile}
    return render(request, 'user/profile.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                pass
        else:
            return ValidationError('Not Allowed')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return ''


def profile_complete(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
