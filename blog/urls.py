from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^recipe/$', views.recipe_list, name='recipe'),
    url(r'^recipe/(?P<pk>\d+)/', views.recipe_detail, name='recipe_detail'),
    url(r'^recipe/new/$', views.recipe_new, name='recipe_new'),
    url(r'^recipe/(?P<pk>\d+)/edit/$', views.recipe_edit, name='recipe_edit'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^order/$', views.order, name='order'),
]
