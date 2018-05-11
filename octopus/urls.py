"""octopus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from octopus.views import HypothesisListView, HypothesisCreate, HypothesisUpdate, HypothesisDelete, PrototypeView


urlpatterns = [
    url(r'^', PrototypeView.as_view()),
    url(r'^hypothesis/', HypothesisListView.as_view()),
    url(r'^hypothesis/add/$', HypothesisCreate.as_view(), name='hypothesis-add'),
    url(r'^hypothesis/(?P<pk>[0-9]+)/$', HypothesisUpdate.as_view(), name='hypothesis-update'),
    url(r'^hypothesis/(?P<pk>[0-9]+)/delete/$', HypothesisDelete.as_view(), name='hypothesis-delete'),
    url(r'^admin/', admin.site.urls),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

]
