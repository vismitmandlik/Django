from django.shortcuts import render, redirect
from crudapp.forms import UserForm
from django.http import HttpResponse
from crudapp.models import User


def insert(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                return HttpResponse("<h1>Data sent to the database...</h1>")
            except:
                return HttpResponse("<h1>Please recheck you have some problem...</h1>")
    else:
        form = UserForm()
        return render(request, "index.html", {"form": form})


def show(request):
    users = User.objects.all()
    return render(request, "show.html", {"users": users})


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/show")


def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, "edit.html", {"user": user})


def update(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return redirect("/show")
    else:
        return render(request, "edit.html", {"user": user})
