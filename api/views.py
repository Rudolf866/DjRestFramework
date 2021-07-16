from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework_api_key.permissions import HasAPIKey

from api.models import Ticket
from api.serializer import TicketSerializer


class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [HasAPIKey]


class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [HasAPIKey]


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [HasAPIKey]