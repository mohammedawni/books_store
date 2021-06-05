from django.contrib import admin
from .models import Book, Review
# Register your models here.

class ReviewInline(admin.TabularInline):
    '''Tabular Inline View for Review'''

    model = Review
 

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    '''Admin View for Book'''
    inlines = [
        ReviewInline,
    ]

    list_display = ('title', 'author', 'price')
    search_fields = ('title',)

