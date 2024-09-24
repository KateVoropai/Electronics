from rest_framework import serializers

from network.models import NetworkElement


class NetworkElementSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = NetworkElement
        fields = '__all__'
        read_only_fields = ['debit', 'created_at']
