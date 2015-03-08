from django.conf.urls import patterns,url
from gjobs import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^user/(?P<user>\w+)/(?P<proj>p\d+)$',views.userindex,name="user"),
    url(r'^user/(?P<user>\w+)/',views.userindex2,name="user"),
    url(r'^group/(?P<group>g\d+)/$',views.groupindex,name="group"),
    url(r'^job/(?P<job>j\d+)/$',views.jobindex,name="job"),
    url(r'^jobs/$',views.jobs,name='jobs'),
    url(r'^jobsjson/$',views.jobsjson,name='jobsjson'),
    )
