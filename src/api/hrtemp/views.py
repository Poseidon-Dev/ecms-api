from hrtemp.models import HRTEMP
from hrtemp.serializers import HRTEMPSerializer
from rest_framework import generics


class HRTEMPList(generics.ListAPIView):
    """
    List all HRTEMP table entries
    """

    queryset = HRTEMP.objects.all()
    serializer_class = HRTEMPSerializer
