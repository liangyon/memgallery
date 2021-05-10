from django.urls import path
from . import views
from .views import SignUp

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('upload_to_user', views.upload_to_user, name='upload_to_user'),
]


