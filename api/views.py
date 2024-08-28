from rest_framework.response import Response # Responsible for returning the response to the user
from rest_framework.decorators import api_view # Responsible for defining the type of request that we want to accept
from core.models import Item
from .serializers import ItemSerializer

# Serialized data is a dictionary that contains the data that we want to return to the user
# We can return a dictionary, a list, or a string
@api_view(['GET'])  # HTTP GET request
def getData(request):
    # person = {'name': 'Mary Claire Ethereal', 'job': 'Software Engineer'}
    # return Response(person) # Will be output as a JSON object
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True) # Setting many to true means that we are serializing multiple items
    return Response(serializer.data) # Will be output as a JSON object

@api_view(['POST']) # HTTP POST request
def addItem(request):
     serializer = ItemSerializer(data=request.data) # We are passing the data that we are receiving from the request

     if serializer.is_valid():
         serializer.save()

     return Response(serializer.data)