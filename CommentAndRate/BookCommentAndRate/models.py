from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'BookCommentAndRate'

class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book.title} ({self.rating}) by {self.user.username} on {self.timestamp}'

class BookComment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book.title} ({self.comment}) by {self.user.username} on {self.timestamp}'
