from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.serializers import PhotoSerializer
from gallery.models import Photo, Favorite


class PhotoList(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class AddFavorite(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        photo_id = pk
        if not photo_id:
            return Response({'error': 'Missing id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            photo = Photo.objects.get(id=photo_id)
        except Photo.DoesNotExist:
            return Response({'error': 'Photo with this id does not exists'}, status=status.HTTP_404_NOT_FOUND)
        favorite, created = Favorite.objects.get_or_create(user=request.user, photo=photo)
        if not created:
            return Response({'error': 'Already in favorite'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PhotoSerializer(photo, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemoveFavorite(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            favorite = Favorite.objects.get(user=request.user, photo__id=pk)
        except Favorite.DoesNotExist:
            return Response({'error': 'Photo is not in favorite'}, status=status.HTTP_400_BAD_REQUEST)
        favorite.delete()
        return Response({'error': 'Photo is deleted from favorite'}, status=status.HTTP_204_NO_CONTENT)
