from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context ={}
    return render(request,'utilities/index.html',context)
def process(request):
    if request.method == 'POST':
        text = request.POST['text']
        process = text.upper()
    return HttpResponse(process)       
