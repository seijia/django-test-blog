"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myblog.views import BlogList,BlogList2,get_detail,ArchivesView,AboutViews,RSSFeed,blog_search,SearchViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', BlogList,name='home'),
    url(r'^detail/(?P<id>\d+)/$',get_detail,name='blog_get_detail'),
    url(r'^blog/$',ArchivesView.as_view(),name='archives'),
    url(r'^about-me/$',AboutViews.as_view(),name='about_me'),
    url(r'^tag/(?P<tag>[\w-]+)/$',SearchViews.as_view(),name='search_tag'),
    url(r'^feed/$',RSSFeed(),name = "RSS"),
    url(r'search/$',blog_search,name='search'),
    url(r'test/$',BlogList2.as_view(),name="pages"),
]
