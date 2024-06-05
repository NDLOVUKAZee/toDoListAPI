from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user=User.objects.create_user('Nomthi', 'nomthi@gmail.com', 'password123!@')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email,'nomthi@gmail.com')

    def test_creates_super_user(self):
        user=User.objects.create_superuser('Nomthi', 'nomthi@gmail.com', 'password123!@')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email,'nomthi@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username="", email='nomthi@gmail.com', password= 'password123!@')


        # user=User.objects.create_user()
        # self.assertIsInstance(user, User)
        # self.assertFalse(user.is_staff)
        # self.assertEqual(user.email,'nomthi@gmail.com')