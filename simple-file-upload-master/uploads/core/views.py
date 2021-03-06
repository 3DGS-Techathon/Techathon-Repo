from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
import pandas as pd
data = []

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        myjson = request.FILES['myjson']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        filenamejson = fs.save(myjson.name, myjson)
        uploaded_json_url = fs.url(filenamejson)
        uploaded_file_url = fs.url(filename)
        print("uploaded_file_url 123 : " +uploaded_file_url)
        data = pd.ExcelFile (myfile) 
        df = data.sheet_names
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'uploaded_json_url': uploaded_json_url,
            "df_sheetName" : df
        })
    return render(request, 'core/simple_upload.html')

def simple(request):
    return render(request, 'core/simple.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })


def validation123(request):
    if request.method == 'POST':
        
        data = request.POST.get("reqdatalist")
        print("done!!!")
        
        return render(request, 'core/simple_upload.html')

print(data)