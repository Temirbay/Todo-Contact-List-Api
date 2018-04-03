from rest_framework import serializers

from api.models import Todo, Contact

class TodoSerializer (serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"

class ContactSerializer (serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"