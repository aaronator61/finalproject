from django.shortcuts import render

from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'pages/index.html')   

def reviewsPageView(request):
    return render(request, 'pages/reviews.html') 

def searchPageView(request):
    return render(request, 'pages/search.html') 

def addPageView(request):
    return render(request, 'pages/add.html') 
    
               
            