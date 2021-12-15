#  MIT License
#
#  Copyright (c) 2021 islam kamel
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.


from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUserModel(TestCase):

    def test_create_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            username='super', nickname='super', email='super@super.com',
            password='super', phone='01066373279')

        self.assertEqual(super_user.username, 'super')
        self.assertEqual(super_user.nickname, 'super')
        self.assertEqual(super_user.email, 'super@super.com')
        self.assertEqual(super_user.phone, '01066373279')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)

        with self.assertRaises(ValueError):
            # is_superuser
            db.objects.create_superuser(
                username='super', nickname='super', email='super@super.com',
                password='super', phone='01066373279', is_superuser=False)
        with self.assertRaises(ValueError):
            # is_staff
            db.objects.create_superuser(
                username='super', nickname='super', email='super@super.com',
                password='super', phone='01066373279', is_staff=False)

    def test_create_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            username='user', nickname='user', email='user@super.com',
            password='user', phone='01066373279')

        self.assertEqual(user.username, 'user')
        self.assertEqual(user.nickname, 'user')
        self.assertEqual(user.email, 'user@super.com')
        self.assertEqual(user.phone, '01066373279')
        self.assertEqual(str(user), 'user')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(ValueError):
            # non username
            db.objects.create_superuser(
                username='', nickname='super', email='super@super.com',
                password='super', phone='01066373279')
        with self.assertRaises(ValueError):
            # non nickname
            db.objects.create_superuser(
                username='super', nickname='', email='super@super.com',
                password='super', phone='01066373279')
        with self.assertRaises(ValueError):
            # non email
            db.objects.create_superuser(
                username='super', nickname='super', email='', password='super',
                phone='01066373279')
