# Python modules
import os, difflib

# Django modules
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import ConfigurationFile
from .forms import CompareConfigForm, UploadConfigForm

def do_diff(file1, file2):
    f1 = open(file1)
    f2 = open(file2)
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    f2.close()
    f1.close()
    
    diff_contents = difflib.HtmlDiff().make_file(
        lines1, 
        lines2,
        os.path.basename(file1),
        os.path.basename(file2),
        context=True,
        numlines=10
    )
    return diff_contents

def handle_uploaded_file(f):
    filename = settings.MEDIA_ROOT / 'uploads' / f.name
    with open(filename, 'wb') as destination:
        # using chunks to prevent FS from being overwhelmed by large files
        # might be possible to do this in some validation somewhere else
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()

class CompareConfigView(FormView):
    form_class = CompareConfigForm
    template_name = "compare.html"
    success_url = "compare_success.html"

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return render(request, 'compare.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_bound and form.is_valid:
            first_file = request.POST.get('first_file_field')
            second_file = request.POST.get('second_file_field')
            diff_contents = do_diff(first_file, second_file)
            return HttpResponse(diff_contents) # requires user to go back via the browser
        else:
            return self.form_invalid(form)
        return render(request, 'compare.html', {'form': form})

class UploadConfigView(FormView):
    form_class = UploadConfigForm
    template_name = "upload.html"
    success_url = "upload_success.html"

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                handle_uploaded_file(f)
                new_config = ConfigurationFile(configuration_file=f)
                new_config.save()
            return HttpResponseRedirect(reverse('upload_success'))
        else:
            return self.form_invalid(form)
        return render(request, 'upload.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def compare_success(request):
    return render(request, 'compare_success.html')

def upload_success(request):
    return render(request, 'upload_success.html')
