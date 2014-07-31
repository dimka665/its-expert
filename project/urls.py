
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from its_expert.views import CreateObjectView

from project import settings


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', CreateObjectView.as_view(), name='create-object'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
