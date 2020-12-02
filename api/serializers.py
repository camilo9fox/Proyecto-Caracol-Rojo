from django.contrib.auth.models import Group
from rest_framework import serializers
from usuarios.models import Usuario


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombre', 'apellido', 'estado', 'credito']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']