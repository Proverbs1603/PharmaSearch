from rest_framework import generics
from drugs_api.serializers import DrugSerializer
from drugs.models import Drug
from django_filters.rest_framework import DjangoFilterBackend

class DrugList(generics.ListCreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['prdlst_nm']