from django.urls import path
from .views import indexPageView, searchPageView, addPageView, reviewsPageView
            
urlpatterns = [
                path("", indexPageView, name="index"),
                path("search/", searchPageView, name= 'search'), 
                path("add/", addPageView, name= 'add'),
                path("reviews/", reviewsPageView, name= 'reviews'),
]                  
            