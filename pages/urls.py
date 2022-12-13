from django.urls import path
from .views import indexPageView, addPageView, reviewsPageView, updateReview
            
urlpatterns = [
                path("", indexPageView, name="index"),
                path("add/", addPageView, name= 'add'),
                path("reviews/", reviewsPageView, name= 'reviews'),
                path('update/<int:id>', updateReview, name='update')
]                  
            