from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import EmailAppForm


def index(request):
    if request.method == "POST":
        form = EmailAppForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("index")
        else:
            return redirect("index")
    else:
        form = EmailAppForm()
    return render(request, "email_app/index.html", {"form":form})

def list(request):
    pass

def add(request):
    pass
