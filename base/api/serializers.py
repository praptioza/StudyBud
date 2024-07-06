# in Django REST Framework, 'serializers.py' is used to define serializers, which are responsible for converting complex data types like Django model instances into native Python data types that can be easily rendered into JSON, XML, or other content types.
# also used to deserialize parsed data back into complex types, after validating the incoming data

from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'