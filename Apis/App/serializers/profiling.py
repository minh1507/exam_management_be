from rest_framework import serializers
from App.models.profiling import Profiling

class ProfilingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profiling
        fields = ('id', 'firstname', 'middlename', 'lastname', 'age')