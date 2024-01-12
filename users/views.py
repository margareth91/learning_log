from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    """Rejestracja nowego uzytkownika"""
    if request.method != "POST":
        # Wyswietlenie pustego formularza rejestracji uzytkownika
        form = UserCreationForm()
    else:
        # Przetworzenie wypelnionego formularza
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST["password1"]
            )
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse("index"))

    context = {"form": form}
    return render(request, "users/register.html", context)
