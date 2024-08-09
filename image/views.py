from django.shortcuts import render
from .forms import ImageForm
from .models import image


def index(request):
    if request.method=="POST":
        form=ImageForm (data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=ImageForm()
    img=image.objects.all()
    dic_from={
              'form':form,
              'img':img
        }
    return render(request,"image.html",dic_from)


