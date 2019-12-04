from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('add/', views.add_post, name='add_post'),

    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),

    path('<slug:slug>/login/', views.post_login, name='post_login'),

    path('<slug:slug>/delete/', views.PostDelete.as_view(), name='post-delete'),

    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),

    path('archive/<int:year>/<str:month>/', views.ArticleMonthArchiveView.as_view(), name="archive_month"),

    path('archive/<int:year>/', views.ArticleYearArchiveView.as_view(), name="article_year_archive"),
]
