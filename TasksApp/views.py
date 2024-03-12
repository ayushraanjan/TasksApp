from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpRequest
from django import forms
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

class NewDoneForm(forms.Form):
    done_task = forms.CharField(label="Done Task")


def index(request):
    if request.method == "POST":
        form1 = NewDoneForm(request.POST)
        if form1.is_valid():
            done_task = str(form1.cleaned_data["done_task"])
            if done_task in request.session["tasks"]:
                request.session["tasks"].remove(done_task)
                request.session.modified = True
                print(f"Removed {done_task}")
            else:
                print(f"Error: Task {done_task} not found in the list.")
                
            
        return HttpResponseRedirect(reverse("TasksApp:index"))
    else:

        
             
        if "tasks" not in request.session:
            request.session["tasks"] = []
        return render(request, "TasksApp/index.html",{
                 
            "tasks":request.session["tasks"]

                })
             
    # return HttpResponse("Some error occurred")

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