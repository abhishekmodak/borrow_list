from abstract.permissions import IsOwner
from rest_framework import viewsets
from rental import models
from rental import serializers

class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.with_overdue()
    serializer_class = serializers.FriendSerializer
    permission_class=[IsOwner]

class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer
    permission_class=[IsOwner]

class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer
    filterset_fields = ('to_who', )
    filterset_fields = {
        'returned': ['exact', 'lte', 'gte', 'isnull']
      }

    # def get_queryset(self):
    #    qs = super().get_queryset()
    #    only_missing = str(self.request.query_params.get('missing')).lower()
    #    if only_missing in ['true', '1']:
    #        return qs.filter(returned__isnull=True)
    #    return qs
