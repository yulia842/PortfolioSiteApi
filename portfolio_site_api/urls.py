from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('blog/', include('blog.urls')),
    path('project/', include('portfolio.urls')),
    path('base/', include('base.urls')),
    path('shop/', include('shop.urls')),
    path('user/', include('users.urls')),
]
