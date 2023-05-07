from django.urls import path
from .views import HomePage, Register, Login, test, logoutuser, delete_image

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', HomePage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name='logout'),
    path('test/', test, name='test'),
    path('delete/', delete_image, name='delete-image'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
