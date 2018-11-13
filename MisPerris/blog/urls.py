from django.conf.urls import include, url
from . import views
from rest_framework import routers
from blog.quickstart import views2

router = routers.DefaultRouter()
router.register(r'users', views2.UserViewSet)
router.register(r'groups', views2.GroupViewSet)


app_name= 'perris'




urlpatterns = [
     
    url(r'^$', views.post_list,name="home"),
    url(r'^usuario$', views.post_list,name="listar"),
    url(r'^postular/$', views.postulante_nuevo, name='postulante_nuevo'),
    url(r'^administrar/$', views.administrador,name="Administar"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
     
]

