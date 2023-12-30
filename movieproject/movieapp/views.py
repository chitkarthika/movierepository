from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from .models import mymovie


# Create your views here.
def index(request):
    movie = mymovie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request,"index.html", context)
def detail(request,movie_id):
   # return HttpResponse("This is movie no: %s" % movie_id)
    m=mymovie.objects.get(id=movie_id)

    return render(request,"detail.html",{'movie':m})
def add_movie(request):
    if request.method == "POST":
        name=request.POST['name']
        yr=request.POST['year']
        ds=request.POST['desc']
        image=request.FILES['img']
        movie=mymovie(name=name,year=yr,desc=ds,img=image)
        movie.save()
        messages.info(request, "Movie added")
    return render(request,"add.html")
def update(request,id):
    
    movie = mymovie.objects.get(id=id)
    form = movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method== 'POST':
        m = mymovie.objects.get(id=id)
        m.delete()
        return redirect('/')
    return render(request,'delete.html')