from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import add_santa
from .models import Santa

# Create your views here.

def index(request):
    list_of_santas = Santa.objects.all()
    form_class = add_santa
    
    # Form post
    if request.method == 'POST':
        form = form_class(data=request.POST)
        
        new_santa = Santa(
            name = request.POST.get('santa_name', ''),
            email = request.POST.get('santa_email', ''),
            wishlist = request.POST.get('santa_wishlist', ''),
            restrictions = request.POST.get('santa_restrictions', ''))
        new_santa.save()
    
    template = loader.get_template('polls/index.html')
    context = {
        'list_of_santas': list_of_santas,
        'form': form_class
    }
    return HttpResponse(template.render(context, request))