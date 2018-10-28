from django.conf.urls import url
from . import views
app_name= 'adopciones'
urlpatterns = [
   url(r'^$', views.adopcion_lista, name="list"),

]