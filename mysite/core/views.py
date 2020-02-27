from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

from .models import Note
from .forms import NewNote

def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note, 'pk': pk})  

# def new_note(request):
#     note = NewNote()
#     return render(request, 'core/new_note.html', {'note': note})

def new_note(request):
    if request.method == "POST":
        note = NewNote(request.POST)
        if note.is_valid():
            post = note.save(commit=False)
            post.save()
            return redirect('notes_detail', pk=post.pk)
    else:
        note = NewNote()
    return render(request, 'core/new_note.html', {'note': note})

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        post = NewNote(request.POST, instance = note)
        if note.is_valid():
            post = note.save(commit=False)
            post.save()
            return redirect('notes_detail', pk=post.pk)
    else:
        note = NewNote(instance=note)
    return render(request, 'core/edit_note.html', {'note': note})

def remove_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes_list')