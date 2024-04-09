from django.shortcuts import render
from django.http import HttpResponse
from .forms import upload_File_form
from .models import Students


# Create your views here.


def geeks_view(request):
    return HttpResponse("<h1>Welcome to Geeks for Geeks</h1>")


def upload_file(request):
    if request.method == 'POST':
        form = upload_File_form(request.POST, request.FILES)
        file = request.FILES['file']
        student = Students.objects.create(diploma= file)
        student.save()
        return HttpResponse("The student with ID " + str(student.pk) + " Has file name" + str(file))
    else:
        form = upload_File_form()
    return render(request, 'administration/upload.html', {'form': form})
