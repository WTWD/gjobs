from django.conf.urls import patterns,url
from gjobs import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^welcom/$',views.welcom,name='welcom'),
    url(r'^jobs/$',views.jobs,name='jobs'),
    url(r'^jobsjson/$',views.jobsjson,name='jobsjson'),
    url(r'^user/$',views.user,name='user'),
    )
