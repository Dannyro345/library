from django.shortcuts import render
from . models import Book
from django.db.models import Count, Max, Min
# Create your views here.

def list_book(request):
def book_list(request):
    book = Book.objects.all()
    book1 = Book.objects.aggregate(Count('title'))
    book2 = Book.objects.order_by('years')
    book3 = Book.objects.aggregate(Min('years'))
    book4 = Book.objects.aggregate(Max('years'))
    book5 = Book.objects.get(pk = 2)
    book6 = Book.objects.values('title').filter(genre = 'romance')
    book7 = Book.objects.values('title').filter(years__gt = 1800)
    book8 = Book.objects.filter(years__lt = 1500).aggregate(Count('title'))
    book9 = Book.objects.values('genre').distinct().count()
    book10 = book.values('genre').annotate(qt=Count('genre'))
    
    return render (request, 'library/list.html', 
    {'book': book, 'book1': book1,'book2': book2, 'book3': book3, 'book4': book4, 
    'book5' : book5,  'book6' : book6, 'book7': book7, 'book8': book8, 'book9': book9, 'book10':book10})
