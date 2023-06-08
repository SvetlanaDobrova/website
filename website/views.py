from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import  messages
from catalog.models import Contacts, Feedback
from django.forms.models import model_to_dict


from .entryForm import entryForm
from .feedbackForm import feedbackForm

def home(request):
    template = loader.get_template("home.html")
    context = {
    }
    return HttpResponse(template.render(context, request))

def aboutUs(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            newFeedback = form.save(commit=False)
            newFeedback.feedbackDate = datetime.now()
            newFeedback.save()
            redirect('aboutUs')
    else:
        form = feedbackForm()

    #fb = Feedback.objects.all().order_by("-feedbackDate")
    feedbacks = [model_to_dict(x) for x in Feedback.objects.all().order_by("-feedbackDate")]
    '''.order_by("-feedbackDate")'''
    template = loader.get_template("aboutUs.html")
    context = {
        "feedbackForm":form,
        "feedbacks":feedbacks
    }
    return HttpResponse(template.render(context, request))
def promotions(request):
    template = loader.get_template("promotions.html")
    context = {
    }
    return HttpResponse(template.render(context, request))
def entry(request):

    if request.method == 'POST':
        form = entryForm(request.POST)
        if form.is_valid():
            newContact = form.save(commit=False)
            newContact.contactTimeStamp = datetime.now()
            newContact.save()
            error_text = "сохранено"
            return redirect('entrySuccess')
        else:
            error_text = "Ошибка!"
    else:
        form = entryForm()
        error_text = ""

    template = loader.get_template("entry.html")
    context = { "form":form,
                "error": error_text}
    return render(request, "entry.html", context)



def entrySuccess(request):
    '''
    template = loader.get_template("entrySuccess.html")
    context = {
        "messages":messages.get_messages(request)
    }
    '''
    return HttpResponse(request.POST)