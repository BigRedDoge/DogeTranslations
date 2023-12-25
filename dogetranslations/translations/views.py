from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Series, Book, WebNovel, Chapter
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.text import slugify


# Create your views here.
class TranslationsList(ListView):
    queryset = Series.objects.order_by('-created_on')
    template_name = 'translations.html'

def home(request):
    active_series = []
    for series in Series.objects.all():
        if Book.objects.filter(series=series, active=True).exists():
            active_series.append(series)
    return render(request, 'index.html', {'series_list': active_series})

class SeriesDetail(DetailView):
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
    

def web_novel_detail(request, web_novel_slug):
    web_novel = get_object_or_404(WebNovel, novel_slug=web_novel_slug)
    chapters = Chapter.objects.filter(web_novel=web_novel)
    return render(request, 'web_novel_detail.html', {'web_novel': web_novel, 'chapters': chapters})


def web_novel_chapter(request, web_novel_slug, chapter_slug):
    web_novel = get_object_or_404(WebNovel, novel_slug=web_novel_slug)
    chapter = get_object_or_404(Chapter, web_novel=web_novel, chapter_slug=chapter_slug)
    return render(request, 'chapter.html', {'chapter': chapter})


@login_required
@user_passes_test(lambda user: user.is_editor)
def add_web_novel(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        author = request.user
        web_novel = WebNovel(title=title, description=description, author=author)
        web_novel.save()
        return render(request, 'add_web_novel.html', {'success': True, 'web_novel': web_novel})
    return render(request, 'add_web_novel.html')


@login_required
@user_passes_test(lambda user: user.is_editor)
def translate(request):
    pass