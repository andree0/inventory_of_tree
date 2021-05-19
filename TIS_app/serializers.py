from django.contrib.auth.models import User
from rest_framework import serializers

from TIS_app.models import (
    Circuit,
    Comment,
    Inventory,
    Photo,
    Species,
    Tree,
    User,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="TIS_app:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class CircuitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Circuit
        fields = ("value", )


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ("name", "location", "author", "principal",
                  "principal_address", "comments", "created", )
        read_only_fields = ("created", )
