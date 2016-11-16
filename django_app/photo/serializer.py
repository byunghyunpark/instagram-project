from rest_framework import serializers

from photo.models import Photo, PhotoComment


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['comment_list'] = CommentSerializer(
            instance.photocomment_set.all(),
            many=True).data
        return ret


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = '__all__'
