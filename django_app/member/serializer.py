from rest_framework import serializers
from .models import MyUser as user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )

