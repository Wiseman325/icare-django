from rest_framework import serializers
from data_manager.models import roomForum  

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = roomForum
        fields = '__all__'  
