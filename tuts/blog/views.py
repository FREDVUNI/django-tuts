from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import article

# Create your views here.
def index(request):
    post = article.objects.all()
    context ={"post" : post}
    return render(request,"blog/index.html",context)
    #return HttpResponse("Finally working.")
def details(request,id):
    post =get_object_or_404(article,pk=id)
    context={"a":post}
    return render(request,"blog/details.html",context)