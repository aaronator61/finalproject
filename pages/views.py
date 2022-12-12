from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm, SearchForm
import datetime as dt

def indexPageView(request):
    form = SearchForm()
    if request.method == 'POST':
        search = request.POST['cruise_liner_name']
        if request.POST['ship_name'] == '':
            search_data = Review.objects.filter(cruise_liner_name=search)  
            context = {
                'data': search_data,
                'form': form
            }
            return render(request, 'pages/reviews.html', context)
        else: 
            shipName = request.POST['ship_name']
            search_data = Review.objects.filter(cruise_liner_name=search, ship_name=shipName)  
            context = {
                'data': search_data,
                'form': form
            }
            return render(request, 'pages/reviews.html', context)
    else:
        context = {
            'form': form
        }
        return render(request, 'pages/index.html', context)   

def reviewsPageView(request):
    data = Review.objects.all()
    form = SearchForm()
    if request.method == 'POST':
        search = request.POST['cruise_liner_name']
        if request.POST['ship_name'] == '':
            search_data = Review.objects.filter(cruise_liner_name=search)  
            context = {
                'data': search_data,
                'form': form
            }
            return render(request, 'pages/reviews.html', context)
        else: 
            shipName = request.POST['ship_name']
            search_data = Review.objects.filter(cruise_liner_name=search, ship_name=shipName)  
            context = {
                'data': search_data,
                'form': form
            }
            return render(request, 'pages/reviews.html', context)
    else:
        context = {
            'data': data,
            'form': form
        }
        return render(request, 'pages/reviews.html', context) 

def addPageView(request):
    if request.method == 'POST':
        review = Review()
        
        review.reviewer_name = request.POST['reviewer_name']
        review.cruise_liner_name = request.POST['cruise_liner_name']
        if request.POST['ship_name'] != '':
            review.ship_name = request.POST['ship_name']
        if request.POST['general_location'] != '':
            review.general_location = request.POST['general_location']
        if request.POST['start_date'] != '':
            review.start_date = dt.date(request.POST['start_date'])
        if request.POST['length_in_days'] != '':
            review.length_in_days = request.POST['length_in_days']
        review.star_rating = request.POST['star_rating']
        if request.POST['comments'] != '':
            review.comments = request.POST['comments']

        review.save()

        return redirect(reviewsPageView)
    else:
        form = ReviewForm()
        context = {
            'form': form
        }
        return render(request, 'pages/add.html', context) 

def UpdateReview(request):
    if request.method == 'POST':
        
        

        review.save()
    return reviewsPageView(request)    
            