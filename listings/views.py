from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', 
                  {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    titles = Listing.objects.all()
    return render (request, "listings/listings.html", 
                   {'titles': titles})
              
def contact(request):
    return render(request, "listings/contact.html")