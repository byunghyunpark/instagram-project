from rest_framework import serializers

from .. import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
