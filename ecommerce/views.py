from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from .forms import *

def home_page_old(request):
    return HttpResponse("Hello World!!")


def home_page(request):
    context = {
        "title": "Its home page.",
        "content": "we are in the home page"
    }
    return render(request, "index.html", context)


def about_page(request):
    context = {
        "title": "Its about page.",
        "content": "we are in the about page"
    }
    return render(request, "index.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {"form": contact_form,
               "title": "Contact",
               "content": "Welcome to the Contact Page"}

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        context['form'] = ContactForm()

    # if request.method == "POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    #         name = request.POST.get('fullname')
    #         rec = request.POST.get('recipients')
    # # else:
    #     return render(request, "contact/view.html")
    # context = {"form": contact_form }
    #
    # # if contact_form.is_valid():
    # #     print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    print("user logged in")
    print(request.user.is_authenticated())              # default django method used to check auth

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print("user ---> %s ",user)
        print(request.user.is_authenticated())
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            # Return an 'invalid login' error message.
            print("errorr")


    return render(request, "auth/login.html", context)


def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})

