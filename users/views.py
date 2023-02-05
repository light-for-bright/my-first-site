from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('note_app:index'))


def register(request):
    """Регистрация нового пользователя"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        "Вход под новым пользователем и перенаправление на домашнюю страницу"
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            auth_user = authenticate(username=new_user.username,
                                     password=request.POST['password1'])
            login(request, auth_user)
            return HttpResponseRedirect(reverse('note_app:index'))
    context = {'form': form}
    return render(request, 'register.html', context)
