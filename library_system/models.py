from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    # book_id는 장고에서 자동으로 생성됨
    title = models.CharField(max_length=200)
    writers = models.CharField(max_length=200)
    book_status = models.BooleanField(default=True) # Available is True -> 대여 가능
    book_location = models.CharField(max_length=200)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Borrowed_book(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    date = models.DateTimeField(default=None)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def borrow(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.book.title

class Evaluation(models.Model):
    # review_id 자동 생성
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.review

class Fav_list(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'book'),)

    def __str__(self):
        return self.book.title
