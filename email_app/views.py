from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import EmailAppForm
from .models import EmailAppModel

def add(request):
    if request.method == "POST":
        form = EmailAppForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("index")
        else:
            return redirect("index")
    else:
        form = EmailAppForm()
    return render(request, "email_app/add.html", {"form":form})

def list(request):
    records = EmailAppModel.objects.all()
    return render(request, "email_app/list.html", {"records":records})

def index(request):
    return render(request, "email_app/index.html", {})
