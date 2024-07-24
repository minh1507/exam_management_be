from rest_framework import serializers
from ..models.ethnic import Ethnic
 
class EthnicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ethnic
        fields = ('id', 'name')