from django.http import HttpResponseRedirect
from django.shortcuts import render
from market.models import Contact2
from market.models import Category, Product

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
    categories = Category.objects.all()
    count_cat = categories.count()
    print(count_cat)
    return render(request,'index.html',{'categories':categories,'count_categories':count_cat})

def suit(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    title = 'Костюмы'
    return render(request,'suit.html',{'title':title,'products':products,'categories':categories})

def cart(request):
    title = 'cart'
    return render(request,'cart.html',{'title':title})