from django.db import models
from mysite import settings


__all__ = [
    'Photo',
    'PhotoTag',
    'PhotoComment',
    'PhotoLike',
]


class Photo(models.Model):
    # 나중에 선언되는 참조값은 문자로 기입하면 오류나지 않는다
    image = models.ImageField(upload_to='photo', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True)
    tags = models.ManyToManyField('PhotoTag', blank=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='PhotoLike',
        related_name='photo_set_like_users'
    )

    def to_dict(self):
        ret = {
            'id': self.id,
            'image': self.author.id,
            'content': self.content,
        }
        return ret


class PhotoTag(models.Model):
    title = models.CharField(max_length=200)


class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


# m2m 모델 아님 단순한 forignkey 참조모델
class PhotoComment(models.Model):
    photo = models.ForeignKey(Photo)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        ret = {
            'id': self.id,
            'photo': self.photo.id,
            'author': self.author.id,
            'content': self.content,
        }
        return ret