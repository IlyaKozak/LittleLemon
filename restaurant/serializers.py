from rest_framework import serializers

from .models import Menu, Booking

class MenuSerilializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerilializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'