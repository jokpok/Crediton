from django.conf.urls import patterns, include, url

urlpatterns = patterns('loans.views',
    
    url('unsecured', 'unsecured_credits', name='unsecured_credits'),
    
    url('test', 'test', name='test'),
    
)