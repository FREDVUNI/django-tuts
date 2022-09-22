from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from . models import Question

def index(request):
    #latest = Question.objects.order_by("-pub_date")[:5]
    #template =loader.get_template('polls/index.html')
    #context={"latest" :latest }
    
    #return HttpResponse(template.render(context,request))

    #alternatively,without using HttpResponse you can bind the return
    latest =Question.objects.order_by('-pub_date')[:5]
    context ={"latest" : latest }
    return render(request,"polls/index.html",context)

def detail(request,question_id):
    #return HttpResponse("You're looking at  a question %s" % question_id)

    #using what is in the model to show details
    question =get_object_or_404(Question,pk=question_id)
    context ={"question":question} 
    return render(request,"polls/detail.html",context)

def results(request,question_id):
    response="This is an answer to the question %s"
    return HttpResponse % question_id
def vote(request,question_id):
    return HttpResponse("You're voting on question %s" % question_id)
    