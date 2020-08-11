from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.models import User
from django.utils import timezone

from .forms import ReviewForm, AddBookForm
from .models import Book, Borrowed_book, Fav_list

from django.db import IntegrityError

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST" and request.user.is_active:
        favorite_books = Fav_list.objects.distinct()

        if 'borrow' in request.POST:
            borrowed_book = Borrowed_book.objects.create(borrower=request.user, book=book, date=timezone.now())
            book.book_status = False
            borrowed_book.save()
            book.save()
            return redirect('book_detail', pk=book.pk)
        if 'add_review' in request.POST:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.book = book
                review.user = request.user
                review.save()
                return redirect('book_detail', pk=book.pk)
            else:
                form = ReviewForm()
            return render(request, 'book_detail.html', {'book': book, 'form': form})
        if 'favorite' in request.POST:
            try:
                favorite_book = Fav_list.objects.create(user=request.user, book=book)
                favorite_book.save()
                return redirect('book_detail', pk=book.pk)
            except IntegrityError as e:
                return render(request, "book_detail.html", {'book': book, "message": "이미 좋아하는 책에 저장된 책입니다"})
        return render(request, 'book_detail.html', {'book': book, 'favorite_books': favorite_books})

    return render(request, 'book_detail.html', {'book': book})

def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.manager_id = request.user.id
            book.save()
            return redirect('home')
    else:
        form = AddBookForm()
    return render(request, 'add_book.html', {'form': form})

def search(request):
    qs = Book.objects.all()

    q = request.GET.get('q', '')  # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q:  # q가 있으면
        qs = qs.filter(title__icontains=q)  # 제목에 q가 포함되어 있는 레코드만 필터링

    return render(request, 'search.html', {
        'qs': qs,
        'q': q,
    })

def favlist(request):
    favorite_books = Fav_list.objects.all()
    return render(request, 'favlist.html', {'favorite_books': favorite_books})

# def add_review_to_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.book = book
#             review.user = request.user
#             review.save()
#             return redirect('book_detail', pk=book.pk)
#     else:
#         form = ReviewForm()
#     return render(request, 'add_review_to_book.html', {'form': form, 'book': book})
