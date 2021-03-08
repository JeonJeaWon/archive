from django.shortcuts import render, get_object_or_404
from .models import Archive

def home(request):
    return render(request, 'home.html')
    
def archivemain(request):
    archives = Archive.objects
    return render(request, 'archivemain.html', {'archives' : archives})

def archivedetail(request, archive_id):
    archive_detail = get_object_or_404(Archive, pk = archive_id)
    return render(request, 'archivedetail.html', {'archive' : archive_detail})

# Create your views here.
