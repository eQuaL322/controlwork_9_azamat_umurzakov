from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from api.views import PhotoList, AddFavorite, RemoveFavorite

urlpatterns = [
    path('photos/', PhotoList.as_view(), name='photo_list'),
    path('login/', obtain_auth_token, name='obtain_auth_token'),
    path('favorites/add/<int:pk>/', AddFavorite.as_view(), name='add_favorite'),
    path('favorites/remove/<int:pk>/', RemoveFavorite.as_view(), name='remove_favorite'),
]
