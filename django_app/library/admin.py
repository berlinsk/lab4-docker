from django.contrib import admin
from .models import Book, Reader, Issue

admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Issue)