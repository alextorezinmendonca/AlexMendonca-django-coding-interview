from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from .forms import SubjectForm

def readAll(request):
    subjects = Subject.objects.all().order_by('name')
    return render(request, 'home.html', context = {'subjects':subjects})

def search(request, id):
    subject = get_object_or_404(Subject, id = id)
    return render(request, 'subject_search.html', context = {'subject':subject})

def update(request, id):
    subject = get_object_or_404(Subject, id = id)
    
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjects')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'update.html', context = {'form':form, 'subject':subject})

def delete(request, id):
    subject = get_object_or_404(Subject, id = id)
    subject.delete()
    return redirect('subjects')

def create(request):    
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')
    else:
        form = SubjectForm()
    return render(request, 'create.html', context = {'form':form})