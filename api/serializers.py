# Serialization
# complex data types (query sets and model instances) -> native Python data types -> rendered into JSON, XML

from rest_framework import serializers
from core.models import *

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__" # This will serialize all the fields in the model