from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Menu, Booking
from .serializers import MenuSerilializer, BookingSerilializer

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerilializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuSerilializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({ 'status': 'success', 'data': serializer.data })
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class SingleMenuItemView(APIView):
    def get(self, request, pk):
        item = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerilializer(item)
        return Response({ 'status': 'success', 'data': serializer.data })
        
class BookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerilializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookingSerilializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({ 'status': 'success', 'data': serializer.data })
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerilializer