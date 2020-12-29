from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Image
from .forms import ImageForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Images'})
    else:
        return redirect('images:images')


@login_required
def images(req):
    tmp = Image.objects.all()
    return render(req, 'images.html', {'images': tmp})


@login_required
def image(req, id):
    tmp = get_object_or_404(Image, id=id)
    return render(req, 'image.html', {'image': tmp, 'page_title': tmp.title})

@permission_required('images.change_image')
def delete(req, id):
    if req.method == 'POST':
        i = Image.objects.get(id=id)
        i.delete()
        return redirect('images:images')
    else:
        a = Image.objects.get(id=id)
        return render(req, 'delete.html', {'image': a, 'id': id})



@permission_required('images.change_image')
def edit(req, id):
    if req.method == 'POST':
        form = ImageForm(req.POST, req.FILES)

        if form.is_valid():
            i = Image.objects.get(id=id)
            i.title = form.cleaned_data['title']
            i.description = form.cleaned_data['description']
            i.path = form.cleaned_data['path']
            i.save()
            return redirect('images:images')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Image.objects.get(id=id)
        form = ImageForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('images.add_image')
def new(req):
    if req.method == 'POST':
        form = ImageForm(req.POST, req.FILES)

        if form.is_valid():
            i = Image(title=form.cleaned_data['title'], description=form.cleaned_data['description'], path=form.cleaned_data['path'], owner=req.user)
            i.save()
            return redirect('images:images')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = ImageForm()
        return render(req, 'new.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('images:images')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
