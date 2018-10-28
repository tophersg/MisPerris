from django.conf.urls import url
from . import views

app_name= 'adopcion'

urlpatterns = [
   url(r'^adoptar$', views.adopcion_lista, name="lista"),

]