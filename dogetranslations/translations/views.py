from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Series, Book


# Create your views here.
class SeriesList(generic.ListView):
    queryset = Series.objects.order_by('-created_on')
    template_name = 'index.html'

class SeriesDetail(generic.DetailView):
    model = Series
    template_name = 'series_detail.html'

    def get_object(self):
        return get_object_or_404(Series, series_slug=self.kwargs['series_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(series=self.object)
        return context
    
def series_detail(request, series_slug):
    series = get_object_or_404(Series, series_slug=series_slug)
    books = Book.objects.filter(series=series)
    return render(request, 'series_detail.html', {'series': series, 'books': books})


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

    def get_object(self):
        return get_object_or_404(Book, book_slug=self.kwargs['book_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        series = get_object_or_404(Series, series_slug=self.kwargs['series_slug'])
        book = get_object_or_404(Book, series=series, book_slug=self.kwargs['book_slug'])
        context['posts'] = Post.objects.filter(book_id=book)
        return context

def book_detail(request, series_slug, book_slug):
    series = get_object_or_404(Series, series_slug=series_slug)
    book = get_object_or_404(Book, series=series, book_slug=book_slug)
    posts = Post.objects.filter(book_id=book)
    return render(request, 'book_detail.html', {'series': series, 'book': book, 'posts': posts})


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_object(self):
        series = get_object_or_404(Series, slug=self.kwargs['series_slug'])
        book = get_object_or_404(Book, series=series, book_slug=self.kwargs['book_slug'])
        return get_object_or_404(Post, book_id=book, post_slug=self.kwargs['post_slug'])