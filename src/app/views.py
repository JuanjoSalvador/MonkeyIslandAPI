from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from app.models import Character, Pirate, Insult
from app.serializers import CharacterSerializer, PirateSerializer, InsultSerializer

class BaseAPIView(viewsets.ViewSet):
    def get(self, request):
        bad_request = True

        if self.mandatory_params:
            for param in request.query_params:
                if param in self.mandatory_params:
                    bad_request = False
        else:
            bad_request = False
        
        return bad_request

class CharactersViewSet(BaseAPIView):
    """
    name: Characters View
    description: 
        Take a look into the list of buccaneers, captains and almost everyone arrived at Melee Island.
    return:
        - type: JSON
        - description: A JSON object with the names of the characters.
    """

    mandatory_params = (None)
    permission_classes = (permissions.AllowAny, )

    def list(self, request):
        if super().get(request=request):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": "I didn't get to be eighty-three by being a jackass!"})

        params = request.GET
        role_filter = params.get('role')

        if role_filter:
            characters = Character.objects.filter(role=role_filter)
        else:
            characters = Character.objects.all()
        
        serializer = CharacterSerializer(characters, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        if super().get(request=request):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": "I didn't get to be eighty-three by being a jackass!"})

        queryset = Character.objects.get(id=pk)
        serializer = CharacterSerializer(queryset)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

class PiratesView(BaseAPIView):
    
    mandatory_params = ()
    permission_classes = (permissions.AllowAny, )

    def list(self, request):
        """
        name: Pirates View
        description: 
            Take a look into the list of buccaneers arrived at Melee Island.
        return:
            - type: JSON
            - description: A JSON object with the names of the pirates and its position.
        """

        if super().get(request=request):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": "I didn't get to be eighty-three by being a jackass!"})

        params = request.GET
        role_filter = params.get('role')

        if role_filter:
            pirates = Pirate.objects.filter(role=role_filter)
        else:
            pirates = Pirate.objects.all()

        serializer = PirateSerializer(pirates, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        if super().get(request=request):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": "I didn't get to be eighty-three by being a jackass!"})

        queryset = Pirate.objects.get(id=pk)
        serializer = PirateSerializer(queryset)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
             
class InsultsView(BaseAPIView):
    """
    name: Insults View
    description: 
        Looks for the correct comeback to the given insult into a pirate fight. At least if your opponent
        is not the Swordmaster!
    params:
        - insult:
            - type: integer
            - description: The insult ID you need to return into.
    return:
        - type: JSON
        - description: A JSON object with the given insult and the properly comeback.
    """
    
    mandatory_params = ('insult',)
    permission_classes = (permissions.AllowAny, )

    def list(self, request) -> Response:

        queryset = Insult.objects.all()
        serializer = InsultSerializer(queryset, many=True)
        
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        if super().get(request=request):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"error": "I didn't get to be eighty-three by being a jackass!"})

        queryset = Insult.objects.get(id=pk)
        serializer = InsultSerializer(queryset)

        return Response(status=status.HTTP_200_OK, data=serializer.data)