from rest_framework import serializers

from api.models import Ticket, IwaterProducts


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class IwaterProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IwaterProducts
        fields = '__all__'