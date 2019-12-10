from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Post, Comment
from django.views.generic.dates import YearArchiveView, MonthArchiveView, WeekArchiveView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Count
import random
from django.core.paginator import Paginator



def post_list(request):

    latest_posts_list = Post.objects.order_by('-published_date')[:5]
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]
    first_career = Post.objects.get_category_posts('Career').annotate(num_likes=Count('likes'))[:1]
    career_list = Post.objects.get_category_posts('Career').annotate(num_likes=Count('likes'))[1:5]
    first_campus = Post.objects.get_category_posts('Campus').annotate(num_likes=Count('likes'))[:1]
    campus_list = Post.objects.get_category_posts('Campus').annotate(num_likes=Count('likes'))[1:5]
    first_islam = Post.objects.get_category_posts('Islam').annotate(num_likes=Count('likes'))[:1]
    islam_list = Post.objects.get_category_posts('Islam').annotate(num_likes=Count('likes'))[1:5]
    prof_interviews_list = Post.objects.get_category_posts('Interviews').annotate(num_likes=Count('likes'))[:3]
    tuts_guides_list = Post.objects.get_category_posts('Tutorials').annotate(num_likes=Count('likes'))[:3]
    others_list = Post.objects.get_category_posts('Others').order_by('-published_date')[:5]
    random_posts = random.sample(list(Post.objects.all()), 5)



    context = {
        'latest_posts_list': latest_posts_list,
        'popular_posts': popular_posts,
        'first_career': first_career,
        'career_list': career_list,
        'first_islam': first_islam,
        'islam_list': islam_list,
        'prof_interviews_list': prof_interviews_list,
        'tuts_guides_list': tuts_guides_list,
        'others_list': others_list,
        'first_campus': first_campus,
        'campus_list': campus_list,
        'random_posts': random_posts,
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    random_posts = random.sample(list(Post.objects.all()), 5)
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.name = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'popular_posts': popular_posts,
        'Post': Post,
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
        'comments': comments,
        'comment_form': comment_form,
        'random_posts': random_posts,
    }
    return render(request, 'blog/post_detail.html', context)


def career_post(request):
    category = 'Career'
    category_list = Post.objects.get_category_posts('Career').order_by('-published_date')
    random_posts = random.sample(list(Post.objects.all()), 5)
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]


    paginator = Paginator(category_list, 4)
    page = request.GET.get('page')
    group = paginator.get_page(page)

    context = {
    'popular_posts': popular_posts,
    'random_posts': random_posts,
    'category_list': category_list,
    'category': category,
    'group': group,
    }
    return render(request, 'blog/category_list.html', context)


def campus_post(request):
    category = 'Campus'
    category_list = Post.objects.get_category_posts('Campus').order_by('-published_date')
    random_posts = random.sample(list(Post.objects.all()), 5)
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]

    paginator = Paginator(category_list, 4)
    page = request.GET.get('page')
    group = paginator.get_page(page)

    context = {
    'popular_posts': popular_posts,
    'random_posts': random_posts,
    'category_list': category_list,
    'category': category,
    'group': group,
    }
    return render(request, 'blog/category_list.html', context)


def islam_post(request):
    category = 'Islam'
    category_list = Post.objects.get_category_posts('Islam').order_by('-published_date')
    random_posts = random.sample(list(Post.objects.all()), 5)
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]

    paginator = Paginator(category_list, 2)
    page = request.GET.get('page')
    group = paginator.get_page(page)


    context = {
    'popular_posts': popular_posts,
    'random_posts': random_posts,
    'category_list': category_list,
    'category': category,
    'group': group,
    }
    return render(request, 'blog/category_list.html', context)


def interview_post(request):
    category = 'Interviews'
    category_list = Post.objects.get_category_posts('Interviews').order_by('-published_date')
    random_posts = random.sample(list(Post.objects.all()), 5)
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]

    
    paginator = Paginator(category_list, 2)
    page = request.GET.get('page')
    group = paginator.get_page(page)


    context = {
    'popular_posts': popular_posts,
    'random_posts': random_posts,
    'category_list': category_list,
    'category': category,
    'group': group,
    }
    return render(request, 'blog/category_list.html', context)


def tutorial_post(request):
    category = 'Tutorials'
    category_list = Post.objects.get_category_posts('Tutorials').order_by('-published_date')
    random_posts = random.sample(list(Post.objects.all()), 5)
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]

    
    paginator = Paginator(category_list, 2)
    page = request.GET.get('page')
    group = paginator.get_page(page)

    context = {
    'popular_posts': popular_posts,
    'random_posts': random_posts,
    'category_list': category_list,
    'category': category,
    'group': group,
    }
    return render(request, 'blog/category_list.html', context)


def others_post(request):
    category = 'Others'
    category_list = Post.objects.get_category_posts('Others').order_by('-published_date')
    random_posts = random.sample(list(Post.objects.all()), 5)
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]

    paginator = Paginator(category_list, 2)
    page = request.GET.get('page')
    group = paginator.get_page(page)

    context = {
    'popular_posts': popular_posts,
    'random_posts': random_posts,
    'category_list': category_list,
    'category': category,
    'group': group,
    }
    return render(request, 'blog/category_list.html', context)


@login_required(login_url='/accounts/login')
def post_login(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        return HttpResponseRedirect(post.get_absolute_url())



@login_required(login_url='/accounts/login')
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        is_liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            is_liked = False
        else:
            post.likes.add(request.user)
            is_liked = True
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        return HttpResponseRedirect(post.get_absolute_url())


@login_required(login_url='/accounts/login')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'blog/post_add.html', {'form': form})


@login_required(login_url='/accounts/login')
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})


        

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')


class PostYearArchiveView(YearArchiveView):
    queryset = Post.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True


class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "pub_date"
    allow_future = True


class PostWeekArchiveView(WeekArchiveView):
    queryset = Post.objects.all()
    date_field = "pub_date"
    week_format = "%W"
    allow_future = True
