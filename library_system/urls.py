from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('book_detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('search/', views.search, name='search'),
    path('favlist/', views.favlist, name='favlist'),
    # path('^book/book_detail/(?P<pk>\d+)/review/$', views.add_review_to_book, name='add_review_to_book')
]
