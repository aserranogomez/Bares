from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^bares/(?P<bares_name_slug>[\w\-]+)/$', views.bares, name='bares'),
    url(r'^add_bares/$', views.add_bares, name='add_bares'),
    url(r'^bares/(?P<bares_name_slug>[\w\-]+)/add_tapas/$', views.add_tapas, name='add_tapas'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^like_bares/$', views.like_bares, name='like_bares'),
    url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'),
    )
