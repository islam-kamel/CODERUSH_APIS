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
#

#  MIT License
#
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#
#

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from requests.auth import HTTPBasicAuth

from .main import MainMethod
from ..models import Posts



class TestPostsApp(TestCase, MainMethod):

    def setUp(self) -> None:
        self.client = APIClient(enforce_csrf_checks=True)
        User.objects.create(username='test', password='1234')

        self.user = User.objects.filter(username='test').first()
        Posts.objects.create(title='post', content='test', create_by_id=self.user.pk)

        self.post = Posts.objects.filter(create_by_id=self.user.pk).first()
        self.url = f'/api/v1/posts/{self.post.slug}-{self.user.pk}/'

    def test_details(self):
        data = Posts.objects.get(title='post')
        user = User.objects.get(username='test')

        self.assertEqual(user.username, 'test')
        self.assertIsInstance(user, User)

        self.assertEqual(data.title, 'post')
        self.assertEqual(data.__str__(), data.title)
        self.assertIsInstance(data, Posts)
        self.assertEqual(data.get_absolute_url(), self.url)

    def test_views(self):
        self.client.login(username='test', password='test')
        response = self.client.get('http://127.0.0.1:8000/api/v1/posts/')
        post_details = self.client.get(self.url)
        post_json = {
            "title": "updated",
            "content": "updated",
            "create_by": self.user.pk
        }
        post_update = self.client.put(self.url, post_json, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(post_details.status_code, 200)
