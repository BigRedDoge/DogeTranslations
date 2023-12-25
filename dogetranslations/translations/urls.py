from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home, name="home"),
    path("translations/", views.TranslationsList.as_view(), name="translations"),
    path("series/<slug:series_slug>/", views.SeriesDetail.as_view(), name="series_detail"), #views.SeriesDetail.as_view()
    path("series/<slug:series_slug>/<slug:book_slug>/", views.BookDetail.as_view(), name="book_detail"), # views.BookDetail.as_view()
    path("series/<slug:series_slug>/<slug:book_slug>/<slug:post_slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("web-novel/<slug:web_novel_slug>/", views.web_novel_detail, name="web_novel"),
    path("web-novel/<slug:web_novel_slug>/<slug:chapter_slug>/", views.web_novel_chapter, name="web_novel_chapter"),
]
