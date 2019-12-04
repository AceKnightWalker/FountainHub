from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='index'),

    # CATEGORIES LINKS - Shows posts by categories
    # Shows all posts under campus
    path('campus/', views.campus_post, name='campus'),
    path('career/', views.career_post, name='career'),
    path('interview/', views.interview_post, name='interview'),
    path('others/', views.others_post, name='others'),
    path('islam/', views.islam_post, name='islam'),
    path('tutorial/', views.tutorial_post, name='tutorial'),

    # Full url would be something like; domainname.com/blog/add
    path('add/', views.add_post, name='add_post'),


    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),

    path('<slug:slug>/delete/', views.PostDelete.as_view(), name='post-delete'),

    path('<slug:slug>/login/', views.post_login, name='post_login'),

    path('<slug:slug>/like/', views.like_post, name='like_post'),

    path('<slug:slug>/', views.post_detail, name='details'),






    #path('archive/<int:year>/<str:month>/', views.EventMonthArchiveView.as_view(), name="archive_month"),

    #path('archive/<int:year>/', views.EventYearArchiveView.as_view(), name="article_year_archive"),
]
