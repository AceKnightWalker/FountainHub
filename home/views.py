from django.shortcuts import render
import random
from news.models import Article
from blog.models import Post
from event.models import Event
from django.http import HttpResponse
from django.db.models import Count

def index(request):
	first_career = Article.objects.order_by('-pub_date')[:1]
	article_list = Article.objects.order_by('-pub_date')[1:5]
	event_list = Event.objects.order_by('-start_date')[:4]
	popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]
	

	context = {
        'article_list': article_list,
        'first_career': first_career,
        'event_list': event_list,
        'popular_posts': popular_posts,
        }



	return render(request, 'home/index.html', context)