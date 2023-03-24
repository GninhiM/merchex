from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', 
                  {'first_band': bands[4]})

def about(request):
    return HttpResponse('<h1> A propos </h1> <p> Nous adorons merch !</p>')

def listings(request):
    titles =Listing.objects.all()
    return HttpResponse(f"""<h1> Page de listing</h1>
                        <p>Nous allons afficher la liste de nos produits sur cette page</>
                        <ul>
                            <li>{titles[0].title}</li>
                            <li>{titles[1].title}</li>
                            <li>{titles[2].title}</li>
                        </ul> """)

def contact(request):
    return HttpResponse('<h1>Contactez nous</h1> <p>Formulaire de contact</p>')
