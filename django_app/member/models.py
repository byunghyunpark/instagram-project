from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class MyUserManager(UserManager):
    pass


class MyUser(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)
    following_users = models.ManyToManyField('self', symmetrical=False, through='Relationship', related_name='user_set_following')
    block_users = models.ManyToManyField('self', symmetrical=False, related_name='user_set_block')

    def __str__(self):
        return self.get_full_name()

    def follow(self, user):
        # 중복 생성 방지
        instance, created = Relationship.objects.get_or_create(
            follower=self,
            followee=user
        )
        return instance

    def unfollow(self, user):
        Relationship.objects.filter(folloer=self, followee=user).delete()

    def friends(self):
        return self.following_users.filter(following_users=self)

    def block(self, user):
        self.block_users.add(user)

    def unblock(self, user):
        self.block_users.remove(user)

    def is_friends(self, user):
        if user in self.friends():
            return True
        return False


class Relationship(models.Model):
    follower = models.ForeignKey(MyUser, related_name='relation_set_follower')
    followee = models.ForeignKey(MyUser, related_name='realtion_set_followee')
    created_date = models.TimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ('follower', 'followee')