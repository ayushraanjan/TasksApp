from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpRequest
from django import forms
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "TasksApp/index.html",{
        "tasks":request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form =NewTaskForm(request.POST)
        if form.is_valid():
            task = str(form.cleaned_data["task"])
            request.session["tasks"].append(task)
            request.session.modified = True
            return HttpResponseRedirect(reverse("TasksApp:index"))
        else:
            return render(request, "TasksApp/add.html", {
        "form" : form

    })
    else:
        return render(request, "Tasksapp/add.html",{
            "form": NewTaskForm()
        })

# Create your views here