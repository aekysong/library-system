from django import forms
from .models import Evaluation, Book


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Evaluation
        fields = ('review',)

class AddBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'writers', 'book_location',)

# class SearchForm(forms):
#     word = forms.Charfield(label='search_word')