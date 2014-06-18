from django.conf.urls import patterns, include, url

urlpatterns = patterns('banks.views',
    
    url('^$', 'banks', name='banks'),
    
)