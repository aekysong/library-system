from django.contrib import admin
from .models import Book, Borrowed_book, Evaluation, Fav_list

# Register your models here.

admin.site.register(Book)
admin.site.register(Borrowed_book)
admin.site.register(Evaluation)
admin.site.register(Fav_list)
