from django.shortcuts import render
from .models import Files

def home_page(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "home.html", {})
    
def files_page(request):
    allFiles = Files.objects.all()
    print(allFiles)
    return render(request, "files.html", {})