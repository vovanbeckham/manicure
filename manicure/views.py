from django.http import HttpResponse
from django.shortcuts import render
from manicure.models import Album, Category

from manicure.form import UploadFileForm



def index(request):
    context = {
        'menu': 'Меню',
        'about': 'О сайте',
        'list' : 'Список',
        'news' : 'Новости',
    }
    count_cat = Category.objects.all()
    print(count_cat)
    dict_photo = {} 
    for num in count_cat:
        photos = Album.objects.filter(cat=num.id)
        dict_photo[num.name] = photos
    print(dict_photo)
    return render(request, 'manicure/index.html', locals())


def upload(request):
    context = {
        'menu': 'Меню',
        'about': 'О сайте',
        'list' : 'Список',
        'news' : 'Новости',
    }
    if request.POST:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = Album(img=form.cleaned_data['img'])
            c = Category.objects.get(pk=2)
            fp.cat = c
            fp.save()
    else:
        form = UploadFileForm()
    
    return render(request, 'manicure/upload.html', locals())
