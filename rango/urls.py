from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.show_category, name='show_category'),
    url(r'^about/', views.about, name='about')
    ]
