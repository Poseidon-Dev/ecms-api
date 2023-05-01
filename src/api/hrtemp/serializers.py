from rest_framework import serializers
from hrtemp.models import HRTEMP


class HRTEMPSerializer(serializers.ModelSerializer):

    class Meta:
        model = HRTEMP
        field = "__all__"
