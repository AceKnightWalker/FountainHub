from django.urls import path
from . import views


app_name = 'event'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),

    path('archive/<int:year>/<str:month>/', views.EventMonthArchiveView.as_view(), name="archive_month"),

    path('archive/<int:year>/', views.EventYearArchiveView.as_view(), name="article_year_archive"),
]