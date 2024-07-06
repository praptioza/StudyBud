from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
# api_view decorator is used to specify which HTTP methods are allowed for a particular view function
# it transforms standard Django view function into a DRF view, making it easier to handle requests and responses in the context of a RESTful API

# Response class is used to create HTTP response that can return JSON data
@api_view(['GET'])
def getRoutes(request):
    # list of strings, each string representing a specific API endpoint and the HTTP method to access it
    routes = [ 
        'GET /api/',
        'GET /api/rooms',    # indicates an endpoint for retrieving a list of rooms
        'GET /api/rooms/:id'  # indicates an endpoint for retrieving a specific room by its id
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)