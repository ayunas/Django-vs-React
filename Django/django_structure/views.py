from django.shortcuts import render
from .models import File
# import .models

def index(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "index.html", {'path': request.path})
    
def files_page(request):
    print("request", request.path)
    options = {
        'django': "django" in request.path
    }
    return render(request, "files.html", options)


# def index(request):
#     context = RequestContext(request)