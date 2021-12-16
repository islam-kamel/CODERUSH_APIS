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
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from posts_apis.models import Posts


class TestPostsAPIView(APITestCase):
    def setUp(self):
        db = get_user_model()

        self.user = db.objects.create_user(
            username='user', nickname='user', email='user@super.com',
            password='user', phone='01066373279')

        self.post = Posts.objects.create(
            title='test post', content='test content',
            image='0_m4ilBBUlxq00O-rI.png', create_by_id=self.user.pk)

        self.post_details_url = reverse('post_details', kwargs={
            'slug': 'test-post', 'pk': self.post.pk})

        self.client = APIClient()
        self.posts_list_url = reverse('posts-list')
        self.token_url = reverse('token-obtain-pair')

    def test_post_model(self):
        self.assertEqual(self.post.get_absolute_url(), self.post_details_url)
        self.assertEqual(str(self.post), 'test post')

        with self.assertRaises(Exception):
            self.post = Posts.objects.create(
                title='test post', content='test content',
                image='0_mI.png', create_by_id=self.user.pk).save()

    def test_create_post(self):
        self.assertEqual(self.post.title, 'test post')
        self.assertEqual(self.post.content, 'test content')
        self.assertEqual(self.post.create_by_id, self.user.pk)
        self.assertEqual(self.post.slug, 'test-post')
        self.assertTrue(self.post.published)

    def test_posts_list_view(self):
        response = self.client.get(self.posts_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['title'], 'test post')
        self.assertEqual(response.json()[0]['content'], 'test content')
        self.assertEqual(response.json()[0]['create_by'], self.user.pk)
        self.assertEqual(response.json()[0]['slug'], 'test-post')

    def test_post_details(self):
        response = self.client.get(self.post_details_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], 'test post')
        self.assertEqual(response.json()['content'], 'test content')
        self.assertEqual(response.json()['create_by'], self.user.pk)
        self.assertEqual(response.json()['slug'], 'test-post')

    def test_update_post(self):
        response = self.client.get(self.post_details_url)

        credentials = {
            "username": 'user',
            "password": 'user'
        }
        x = self.client.post(self.token_url, credentials)

        # 'Authorization': 'Bearer '+x.json()['access']
        t = 'Bearer ' + x.json()['access']

        self.client.credentials(HTTP_AUTHORIZATION=t)

        update_data = {
            'title': 'Update',
            'content': 'content',
            'slug': '',
            'create_by': response.json()['create_by']
        }
        update = self.client.put(
            self.post_details_url, data=update_data)

        self.post_details_url = reverse('post_details', kwargs={
            'slug': 'update', 'pk': update.json()['id']})

        response = self.client.get(self.post_details_url)

        self.assertEqual(update.status_code, 200)
        self.assertEqual(response.json()['title'], 'Update')
        self.assertEqual(response.json()['content'], 'content')
        self.assertEqual(response.json()['create_by'], self.user.pk)
        self.assertEqual(response.json()['slug'], 'update')

    def test_delete_post(self):
        self.post = Posts.objects.create(
            title='test Delete', content='test content',
            create_by_id=self.user.pk)

        self.post_details_url = reverse('post_details', kwargs={
            'slug': 'test-delete', 'pk': self.post.pk})

        credentials = {
            "username": 'user',
            "password": 'user'
        }
        x = self.client.post(self.token_url, credentials)

        # 'Authorization': 'Bearer '+x.json()['access']
        t = 'Bearer ' + x.json()['access']

        self.client.credentials(HTTP_AUTHORIZATION=t)

        response = self.client.delete(self.post_details_url)

        self.assertEqual(response.status_code, 200)

    def test_create_post_api_view(self):
        credentials = {
            "username": 'user',
            "password": 'user'
        }
        x = self.client.post(self.token_url, credentials)

        # 'Authorization': 'Bearer '+x.json()['access']
        t = 'Bearer ' + x.json()['access']

        self.client.credentials(HTTP_AUTHORIZATION=t)
        data = {
            'title': 'Test',
            'content': 'Test',
            'slug': '',
            'create_by': self.user.pk
        }

        response = self.client.post(self.posts_list_url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['title'], 'Test')
        self.assertEqual(response.json()['content'], 'Test')
        self.assertEqual(response.json()['create_by'], self.user.pk)
        self.assertEqual(response.json()['slug'], 'test')
