from django.shortcuts import render

def home_page(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "home.html", {})
    