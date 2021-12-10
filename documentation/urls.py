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
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view, SwaggerUIRenderer
from rest_framework import permissions

SwaggerUIRenderer.template = 'drf_yasg.html'

schema_view = get_schema_view(
    openapi.Info(
        title='CODERUSH',
        default_version='v1.0.0',
        description='API developers hoping to use our service.',
        contact=openapi.Contact(email="islam.kamel@agr.suv.eud.eg",
                                name='Islam Kamel'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),

)
urlpatterns = [
   path('', schema_view.with_ui('swagger',  cache_timeout=0))
]
