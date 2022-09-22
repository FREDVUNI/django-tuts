from django.shortcuts import render
from .models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    getItems = Todo.objects.all().order_by('-date_added')
    context ={'item':getItems}
    return render(request,'todo/index.html',context)
def add(request):
    #if request.method == "POST":
    text = request.POST['text']
    date = timezone.now()

    add_item = Todo.objects.create(
        text =text,
        date_added = date
    )
    count = Todo.objects.all().count()    
    return HttpResponseRedirect('/todo') 

def delete_item(request,Todo_id):
    delete = Todo.objects.get(id = Todo_id).delete()
    return HttpResponseRedirect('/todo')        
