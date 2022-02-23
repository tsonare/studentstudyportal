from django.shortcuts import render, redirect
from .models import Note
from .forms import *
from django.contrib import messages
from django.views.generic import DetailView

# Create your views here.


def home(request):
    return render(request, 'dashboard/home.html')


def notes(request):
    if request.method == "POST":
        form = Notesform(request.POST)
        if form.is_valid():
            notes = Note(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request, f"Note saved from {request.user.username} successfully.")

    else:
        form = Notesform()
    notes = Note.objects.filter(user=request.user)
    context = {'notes': notes,'form': form}
    return render(request, 'dashboard/notes.html', context)


def delete_note(request,pk=None):
    Note.objects.get(id=pk).delete()
    return redirect("notes")


class NotesDetailView(DetailView):
    model = Note
    template_name = 'dashboard/notes_detail.html'


