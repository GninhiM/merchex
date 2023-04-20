from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    # récupération des données à partir du model Band qui retourne des objets
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', 
                  {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def listing(request):
    titles = Listing.objects.all()
    return render (request, "listings/listings.html", 
                   {'titles': titles})
              
def contact(request):
    return render(request, "listings/contact.html")