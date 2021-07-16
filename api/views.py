import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework_api_key.permissions import HasAPIKey

from api.models import Ticket, IwaterProducts
from api.serializer import TicketSerializer, IwaterProductsSerializer


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


## **************  Variant II ************** ##

@api_view(['GET', 'POST'])
def iwaterProducts_list(request):
    permission_classes = [HasAPIKey]
    if request.method == 'GET':
        iwaterProducts = IwaterProducts.objects.all()
        title = request.query_params.get('title', None)
        if title is not None:
            iwaterProducts = iwaterProducts.filter(title__icontains=title)

        iwaterProducts_serializer = IwaterProductsSerializer(iwaterProducts, many=True)
        return HttpResponse(json.dumps(iwaterProducts_serializer.data, ensure_ascii=False),
                            content_type="application/json;charset=utf-8")
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        iwaterProducts_data = JSONParser().parse(request)
        iwaterProducts_serializer = IwaterProductsSerializer(data=iwaterProducts_data)
        if iwaterProducts_serializer.is_valid():
            iwaterProducts_serializer.save()
            return HttpResponse(json.dumps(iwaterProducts_serializer.data, ensure_ascii=False),
                                content_type="application/json;charset=utf-8")
        return JsonResponse(iwaterProducts_serializer.errors, status=status.HTTP_400_BAD_REQUEST,
                            content_type="application/json;charset=utf-8")


@api_view(['GET', 'PUT', 'DELETE'])
def iwaterProducts_detail(request, pk):
    permission_classes = [HasAPIKey]
    try:
        iwaterProducts = IwaterProducts.objects.get(pk=pk)
    except IwaterProducts.DoesNotExist:
        return JsonResponse({'message': 'The driver does not exist'}, status=status.HTTP_404_NOT_FOUND,
                            content_type="application/json;charset=utf-8")

    if request.method == 'GET':
        iwaterProducts_serializer = IwaterProductsSerializer(iwaterProducts)
        return HttpResponse(json.dumps(iwaterProducts_serializer.data, ensure_ascii=False),
                            content_type="application/json;charset=utf-8")

    elif request.method == 'PUT':
        iwaterProducts_data = JSONParser().parse(request)
        iwaterProducts_serializer = IwaterProductsSerializer(iwaterProducts, data=iwaterProducts_data)
        if iwaterProducts_serializer.is_valid():
            iwaterProducts_serializer.save()
            return HttpResponse(json.dumps(iwaterProducts_serializer.data, ensure_ascii=False),
                                content_type="application/json;charset=utf-8")
        return JsonResponse(iwaterProducts_serializer.errors, status=status.HTTP_400_BAD_REQUEST,
                            content_type="application/json;charset=utf-8")


    elif request.method == 'DELETE':
        iwaterProducts.delete()
        return JsonResponse({'message': 'Driver was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT,
                            content_type="application/json;charset=utf-8")
