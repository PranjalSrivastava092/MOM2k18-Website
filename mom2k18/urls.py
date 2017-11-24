from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^events$', views.events, name='events'),
    url(r'^mad$', views.mad, name='mad'),
    url(r'^brainwave$', views.brainwave, name='brainwave'),
    url(r'^hospi$', views.hospi, name='hospi'),
    #url(r'^osd$', views.osd, name='osd'),
    url(r'^quiz$', views.quiz, name='quiz'),
    url(r'^sponsors$', views.sponsors, name='sponsors'),
    url(r'^team$', views.team, name='team'),
    url(r'^tme$', views.tme, name='tme'),
    url(r'^cultural$', views.cultural, name='cultural'),
    url(r'^message', views.message, name='message'),
    url(r'^one', views.one, name='1'),
    url(r'^register$', views.register.as_view(), name='register'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^rangmanch$', views.rangmanch, name='rangmanch'),
    url(r'^bandwars$', views.bandwars, name='bandwars'),
    ]