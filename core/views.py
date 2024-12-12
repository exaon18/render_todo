from django.shortcuts import render,redirect
from .models import todo

# Create your views here.
def index(request):
    if request.method =="POST":
        todor=request.POST["todo"]
        newtodo=todo(todo=todor)
        newtodo.save()
        return redirect("index")
    else:
        todos=todo.objects.all()
        return render(request,"index.html",{
            "todo":todos
        })


