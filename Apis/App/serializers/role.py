from rest_framework import serializers
from App.models.role import Role

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'code')

                
        