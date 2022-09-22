from django.shortcuts import get_object_or_404,render
from .models import company
# Create your views here.

def index(request):
    call =company.objects.all()
    context ={"company":call}
    return render(request,"company/index.html",context)

def details(request,id):
    details =get_object_or_404(company,pk=id)
    context={"company":details}
    return render(request,"company/details.html",context)