from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
    return render(request, 'index.html')


def search(request):

    if request.method == "POST":

        search_data = request.POST['search']

        books = Book.objects.filter(name__icontains=search_data)

        context = {
            'books': books
        }

        return render(request, 'search.html', context)
