from django.contrib.auth.models import User, Group
from rest_framework import serializers
from adopcion.models import Perritos


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="perris:user-detail")
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PerritosSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Perritos
        fields = ('titulo','descripcion','fecha_publicacion','thumb')