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

from django.contrib.auth.models import User

from ..models import Posts


class MainMethod:
    def __init__(self):
        self.user = None
        self.post = None

    def create_user(self, username=None, password=None):
        self.user = User.objects.create(username=username, password=password)

    def create_post(self, **kwargs):
        title = kwargs.pop('title')
        content = kwargs.pop('content')
        auth = kwargs.pop('user')

        self.post = Posts.objects.create(title=title, content=content,
                                         create_by_id=auth,
                                         image='D:\my-developer\CodeRushWebApp\CODERUSH_DRF\media\posts\996ad860-2a9a-504f-8861-aeafd0b2ae29.jpg'
                                         )
