from django.shortcuts import render
from .models import Book, Reader, Issue

def index(request):
    issues = Issue.objects.select_related('reader', 'book')
    books = Book.objects.all()
    readers = Reader.objects.all()
    return render(request, 'library/index.html', {
        'books': books,
        'readers': readers,
        'issues': issues
    })