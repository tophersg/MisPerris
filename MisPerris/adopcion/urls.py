from django.conf.urls import url
from . import views

app_name= 'adopcion'

urlpatterns = [
   url(r'^adoptar/$', views.adopcion_lista, name="lista"),
   url(r'^rescate/$', views.rescate_nuevo, name='rescate_nuevo'),
   url(r'^(?P<titulo>[\w-]+)/$', views.adopcion_detalles, name="detalles"),
   url(r'^delete/$', views.rescate_borrar, name='rescate_borrar'),
]