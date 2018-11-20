from django.http import HttpResponse
from django.shortcuts import render


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
 
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('fullname')
        context = {
            "title": "Its contact page.",
            "content": "we are in the contact page",
            "fullname": name
        }
        
    return render(request, "contact/view.html", context)
