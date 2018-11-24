from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'', include('blog.urls')),
    url(r'^$',views.home)
]
