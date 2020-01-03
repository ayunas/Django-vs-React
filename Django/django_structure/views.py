from django.shortcuts import render
from .models import File
# import .models

def index(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "index.html", {})
    
def files_page(request):
    # allFiles = File.objects.all()
    filteredfiles = File.objects.filter(parent_id = 1)
    print(filteredfiles)
    return render(request, "files.html", {})


# def index(request):
#     context = RequestContext(request)