from django.conf.urls import include, url
from . import views

app_name= 'perris'

urlpatterns = [
    url(r'^$', views.post_list,name="home")
]

