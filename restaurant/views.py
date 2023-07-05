from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Menu, Booking
from .serializers import MenuSerilializer, BookingSerilializer

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerilializer

    def get_permissions(self):
        request_method = self.request.method
        is_authenticated = self.request.user.is_authenticated

        if request_method == 'GET' or is_authenticated:
            return []
        raise PermissionDenied()

class SingleMenuItemView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerilializer

    def get_permissions(self):
        request_method = self.request.method
        is_authenticated = self.request.user.is_authenticated

        if request_method == 'GET' or is_authenticated:
            return []
        raise PermissionDenied()
    
class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerilializer