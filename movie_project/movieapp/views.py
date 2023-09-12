from django.shortcuts import render, redirect

from movieapp.form import Movie_Form
from movieapp.models import Movies


# Create your views here.
def index(request):
        obj = Movies.objects.all()
        return render(request,'index.html',{'res':obj})

def details(request,movie_id):
        obj = Movies.objects.get(id=movie_id)
        return render(request,'details.html',{'res':obj})

def movie_add(request):

                if request.method == "POST":
                                name = request.POST['name']
                                img = request.FILES['img']
                                desc = request.POST['desc']

                                movie = Movies(name=name,img=img,desc=desc)
                                movie.save()
                return render(request,'add.html')


def update(request,movie_id):
            movie = Movies.objects.get(id=movie_id)
            form = Movie_Form(request.POST or None,request.FILES,instance=movie)

            if form.is_valid():
                    form.save()
                    return redirect('/')

            return render(request, 'update.html',{'form':form,'movie':movie})


def delete(request,movie_id ):
        if request.method=='POST':
                movie = Movies.objects.get(id=movie_id)
                movie.delete()
                return redirect('/')

        return render(request,'delete.html')
