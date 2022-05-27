from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from market.models import Contact2

# Create your views here.
def base(request):
    return render(request, 'base.html')

def sendContact(request):
    if request.method == 'POST':
        contact = Contact2()
        contact.email = request.POST.get('email')
        contact.name = request.POST.get('name')
        contact.address = request.POST.get('address')
        contact.message = request.POST.get('message')
        contact.save()
        return HttpResponseRedirect('/')
def homepage(request):
    return HttpResponse('hello')