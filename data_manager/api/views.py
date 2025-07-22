from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RoomSerializer
from data_manager.models import roomForum

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',  # List all routes
        'GET /api/room',  
        'GET /api/room/:id', 
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    room = roomForum.objects.all()
    serializer = RoomSerializer(room, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = roomForum.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
