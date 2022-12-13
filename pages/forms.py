from django import forms
from .models import Review
import datetime as dt

years = []
for i in range(int(dt.date.today().year), int(dt.date.today().year) - 50, -1):
    years.append(i)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = 'reviewer_name', 'cruise_liner_name', 'ship_name', 'general_location', 'month', 'length_in_days', 'star_rating', 'comments'
        widgets = {
            # 'start_date': forms.SelectDateWidget(years=years),
            'comments': forms.Textarea(attrs={'rows': 5})
        }

    ship_name = forms.CharField(required=False)
    general_location = forms.CharField(required=False)
    # month = forms.IntegerField(required=False)
    length_in_days = forms.IntegerField(required=False)
    comments = forms.CharField(required=False)

class SearchForm(forms.ModelForm):

    ship_name = forms.CharField(required=False)

    class Meta:
        model = Review
        fields = ('cruise_liner_name','ship_name')
        
