from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from .models import Article
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView
from django.urls import reverse
from .forms import CommentForm, PostForm
from django.utils import timezone
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


class IndexView(generic.ListView):
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('-pub_date')[:5]

@login_required(login_url='/accounts/login')
def post_login(request, slug):
    post = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        post = get_object_or_404(Article, id=request.POST.get('post_id'))
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        return HttpResponseRedirect(post.get_absolute_url())


@login_required(login_url='/accounts/login')
@permission_required('news.add_article', raise_exception=True)
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            post.reporter = request.user
            post.pub_date = timezone.now()
            post.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'news/news_add.html', {'form': form})


@login_required(login_url='/accounts/login')
@permission_required('news.edit_article', raise_exception=True)
def edit_post(request, slug):
    post = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.reporter = request.user
            post.pub_date = timezone.now()
            post.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)
    return render(request, 'news/article_edit.html', {'form': form, 'post': post})


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'news.delete_article'
    model = Article
    success_url = reverse_lazy('news:index')



class DetailView(FormMixin, generic.DetailView):
    model = Article
    form_class = CommentForm

    def get_success_url(self):
        return reverse('news:detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'article': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.name = self.request.user
        obj.article = Article.objects.get(slug=self.kwargs['slug'])
        form.save()
        return super(DetailView, self).form_valid(form)

class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True
