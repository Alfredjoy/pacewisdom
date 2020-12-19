from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    image = Images.objects.all()
    cate = Images.objects.values_list('Category', flat=True)
    cat = []

    for c in cate:
        cat.append(c)

    cat = list(dict.fromkeys(cat))
    context = {'images': image, 'cats': cat}

    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        cat = request.POST.get('category')
        photo = request.FILES['photo']
        fs = FileSystemStorage()  # filesystemstorage?
        fs.save(photo.name, photo)
        a=Images()
        a.Name = name
        a.Desc = desc
        a.Category = cat
        a.image=photo
        a.save()

        image = Images.objects.all()
        cate = Images.objects.values_list('Category', flat=True)
        cat = []

        for c in cate:
            cat.append(c)

        cat = list(dict.fromkeys(cat))
        context = {'images': image,'cats':cat}

        return render(request, 'home.html', context)

    return render(request,'home.html', context)

def category(request,id):
    cats = id

    image = Images.objects.filter(Category=cats)

    context = {'images': image, 'cats': cats}
    if request.method == 'POST':
        if request.method == 'POST':
            name = request.POST.get('name')
            desc = request.POST.get('desc')
            cat = request.POST.get('cats')
            photo = request.FILES['photo']
            fs = FileSystemStorage()  # filesystemstorage?
            fs.save(photo.name, photo)
            a = Images()
            a.Name = name
            a.Desc = desc
            a.Category = cat
            a.image = photo
            a.save()

            image = Images.objects.all()
            cate = Images.objects.values_list('Category', flat=True)
            cat = []

            for c in cate:
                cat.append(c)

            caty = list(dict.fromkeys(cat))
            context = {'images': image, 'cats': caty}

            return render(request, 'home.html', context)

    return render(request, 'category.html', context)

def new_category(request):
    image = Images.objects.all()
    cats = Images.objects.values_list('Category', flat=True)
    cat = []

    for cat in cats:
        cat.append(cat)

    cat = list(dict.fromkeys(cat))
    context = {'images': image, 'cats': cat}
    if request.method == 'POST':
        if request.method == 'POST':
            name = request.POST.get('name')
            desc = request.POST.get('desc')
            cat = request.POST.get('cats')
            photo = request.FILES['photo']
            fs = FileSystemStorage()  # filesystemstorage?
            fs.save(photo.name, photo)
            a = Images()
            a.Name = name
            a.Desc = desc
            a.Category = cat
            a.image = photo
            a.save()

            image = Images.objects.all()
            cate = Images.objects.values_list('Category', flat=True)
            cat = []

            for c in cate:
                cat.append(c)

            cat = list(dict.fromkeys(cat))
            context = {'images': image, 'cats': cat}

            return render(request, 'home.html', context)


    return render(request,'new_category.html',context)




