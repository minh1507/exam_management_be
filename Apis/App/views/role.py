from rest_framework import viewsets, mixins
from App.models import Role
from App.serializers import RoleSerializer
from App.commons.response import ResponseReadMany
class RoleView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def list(self, request, pk=None):
        roles = Role.objects.exclude(code="ADMIN").all()
        serializer = RoleSerializer(roles, many=True)

        return ResponseReadMany(
            data=serializer.data,
            total_count=len(serializer.data)
        ).to_response()
    
        