from .models import Book, BookInstance, Author
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'

class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'

class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    template_name = 'catalog/author_list.html'

def index(request):
    """View function for the home page."""
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    # Track visits using session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context)