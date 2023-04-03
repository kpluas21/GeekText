from django import forms

class CommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea)
    user_id = forms.IntegerField()
    book_id = forms.IntegerField()

class RatingForm(forms.Form):
    value = forms.ChoiceField(choices=((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')))
    user_id = forms.IntegerField()
    book_id = forms.IntegerField()
