from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Shop, Listing
from .serializers import ShopSerializer, ListingSerializer
#Create your views here

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    @action(detail=True, methods=['get'])
    def listings(self, request, pk=None):
        shop = self.get_object()
        listings = shop.listings.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        queryset = self.get_queryset()
        title = request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        serializer = ListingSerializer(queryset, many=True)
        return Response(serializer.data)
