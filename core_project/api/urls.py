from .views import *
from django.urls import path, include


urlpatterns = [
    path('std/<id>', Std_Api.as_view()),
    path('register/', RegisterUser.as_view(), name='register'),

    # path('', home, name='home'),
    # # path('post-std/', post_std, name='post_std'),
    # # path('put-std/<id>', put_std, name='put_std'),
    # # path('patch-std/<id>', patch_std, name='patch_std'),
    # # path('del-std/', delete_std, name='delete_std'),


]