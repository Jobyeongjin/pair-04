from django.forms import ModelForm
from .models import Review, Comment



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = (
            'title',
            'content',
            'movie_name',
            'grade',
        )

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = (
            'user',
            'review',
        )