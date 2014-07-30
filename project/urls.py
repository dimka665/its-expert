
from django.conf.urls import patterns, include, url
from django.contrib import admin

from its_expert.views import CreateObjectXView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', CreateObjectXView.as_view(), name='create-object-x'),

    url(r'^admin/', include(admin.site.urls)),
)
