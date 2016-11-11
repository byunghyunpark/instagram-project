from django.test import TestCase, LiveServerTestCase
from .models import MyUser


class FollowTest(LiveServerTestCase):
    def create_user(self, username, last_name, first_name):
        return MyUser.objects.create_user(
            username=username,
            last_name=last_name,
            first_name=first_name,
        )

    def test_create_user(self):
        print('test_create_user')
        u1 = self.create_user('u1', '방', '민아')
        u2 = self.create_user('u2', '이', '한영')
        u3 = self.create_user('u3', '박', '병현')

    def test_follow_user(self):
        print('test_create_user')
        u1 = self.create_user('u1', '방', '민아')
        u2 = self.create_user('u2', '이', '한영')
        u3 = self.create_user('u3', '박', '병현')

        u2.follow(u1)
        u3.follow(u2)
        u3.follow(u1)
        u2.follow(u1)

        print(u2.following_users.all())
        print(u3.following_users.all())

        u1_friends = u1.following_users.filter(following_users=u1)
        u2_friends = u2.following_users.filter(following_users=u2)

        print(u1_friends)
        print(u2_friends)
