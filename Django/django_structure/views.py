from django.shortcuts import render
from .models import File
# import .models

def index(request, *args, **kwargs):
    print(args, kwargs)
    # filteredfiles = File.objects.filter()
    data = File.objects.all()
    return render(request, "index.html", {'data' : data})
    
def files_page(request):
    # allFiles = File.objects.all()
    filteredfiles = File.objects.filter(parent_id = 1)
    print('type of filtered files', filteredfiles)
    return render(request, "files.html", {'filteredfiles': filteredfiles})


# def index(request):
#     context = RequestContext(request)