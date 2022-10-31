
from django.http import HttpResponse
# Create your views here.
def indexPageView(request) :
    return HttpResponse('Hello Universe!')   

def reviewsPageView(request):
    return HttpResponse("These are our reviews!")

def searchPageView(request):
    return HttpResponse("Search our reviews!")

def addPageView(request):
    return HttpResponse("Add to our reviews!")
    
               
            