from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .models import Blog
from .forms import Commentform
from django.http import Http404,HttpResponseRedirect,HttpResponse
from .models import Comment
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView,ListView,FormView
from django.views.generic.detail import SingleObjectMixin

from .models import Blog
# Create your views here.


class BlogList2(ListView):
    # queryset = Blog.objects.order_by("create")
    template_name = "Test.html"
    queryset = Blog.objects.all()
#



def BlogList(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs,2)

    page = request.GET.get('page')

    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)

    return render(request,'home.html',{'blog_list':blog_list})


# class ContactView(FormView,ListView):
#     template_name = "detail.html"
#     form_class = Commentform
#     success_url = '/detail/'
#     context_object_name = 'blog'
#
#     def get_queryset(self):
#         self.article = get_object_or_404(Blog,id = self.kwargs["id"])
#         return self.article
#
#     def get_context_data(self, **kwargs):
#         context = super(ContactView, self).get_context_data(**kwargs)
#         context["comments"] = self.blog.comment_set.all().order_by('-create')
#         return context
#
#     def form_valid(self, form):
#         self.cd = form.cleaned_data
#         self.cd['blog'] = self.blog
#         Comment.objects.create(**self.cd)
#         return super(ContactView, self).form_valid(form)




def get_detail(request,id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404


    if request.method == 'GET':
        form = Commentform(initial={'content':'请输入评论'})
    else:
        form = Commentform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cd['blog']=blog
            Comment.objects.create(**cd)
            return HttpResponseRedirect('/detail/'+id)


    ctx = {
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-create'),
        'form':form
    }

    return render(request,'detail.html',ctx)


class ArchivesView(ListView):
    template_name = 'blog.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Blog.objects.all()
        context['error'] = False
        return context


# def archives(request):
#     try:
#         blog_list = Blog.objects.all()
#     except Blog.DoesNotExist:
#         raise Http404
#
#     return render(request, 'blog.html', {'post_list':blog_list,'error':False})


class AboutViews(ListView):
    template_name = "about_me.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SearchViews(ListView):
    template_name = "search_tag.html"

    def get_queryset(self):
        self.blog = get_list_or_404(Blog, category=self.kwargs["tag"])
        return self.blog

    def get_context_data(self,*args,**kwargs):
        context = super(SearchViews, self).get_context_data(*args,**kwargs)
        context["num"] = Blog.objects.category_count(self.kwargs["tag"])
        return context


def search(request,tag):
    try:
        blog_list = Blog.objects.filter(category=tag).order_by("-create")
        num = Blog.objects.category_count(tag)
    except Blog.DoesNotExist:
        raise Http404

    return render(request,'search_tag.html',{'blog_list':blog_list,'num':num})


class RSSFeed(Feed):
    title = "RSS Feed - blog"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Blog.objects.order_by("-create")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return "127.0.0.1:8000/detail/"+str(item.id)+"/"
            #"xgjava.com/essay/"+str(item.id)+"/"


def blog_search(request):
    if 's' in request.GET:
        s=request.GET['s']
        if not s:
            return redirect('/home/')
        else:
            post_list = Blog.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'blog.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'blog.html', {'post_list' : post_list,
                                                    'error' : False})





