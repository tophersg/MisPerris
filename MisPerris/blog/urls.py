from django.conf.urls import include, url
from . import views

app_name= 'perris'

urlpatterns = [
    url(r'^$', views.post_list,name="home"),
    url(r'^usuario$', views.post_list,name="listar"),
    url(r'^postular/$', views.postulante_nuevo, name='postulante_nuevo'),
    url(r'^administrar/$', views.administrador,name="Administar"),
]