from . import views
from django.urls import path

urlpatterns = [
    path("", views.SeriesList.as_view(), name="home"),
    path("series/<slug:series_slug>/", views.series_detail, name="series_detail"), #views.SeriesDetail.as_view()
    path("series/<slug:series_slug>/<slug:book_slug>/", views.book_detail, name="book_detail"), # views.BookDetail.as_view()
    path("series/<slug:series_slug>/<slug:book_slug>/<slug:post_slug>/", views.PostDetail.as_view(), name="post_detail"),
]
