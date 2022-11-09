from django.shortcuts import render
#from .forms import UploadFileForm
#from django.http import HttpResponseRedirect

from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.

'''
def handle_upload_file(file):
    with open('../UploadedFiles/{}'.format(file.name),'wb+') as destination:
        for chunk in file.chunks:
            destination.write(chunk)

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['myfile'])
            return HttpResponseRedirect('/success/url')
    else:
        form = UploadFileForm()
    return render(request,'upload.html',{'form':form})
    '''

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        uploaded_file_url = fs.url(filename)
        return render(request,'upload.html',{'uploaded_file_url': uploaded_file_url})
    return render(request,'upload.html')