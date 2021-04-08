from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from historiarum.models import Fabula
from .serializers import FabulaSerializer


class FabulaListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # historiarum = Fabula.objects.filter(user=request.user.id)
        historiarum = Fabula.objects.all()
        serializer = FabulaSerializer(historiarum, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'titulus': request.data.get('titulus'),
            'contentus': request.data.get('contentus'),
            'user': request.user.id,
        }
        serializer = FabulaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FabulaDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, fabula_id, user_id):
        try:
            return Fabula.objects.get(id=fabula_id, user=user_id)
        except Fabula.DoesNotExist:
            return None

    def get(self, request, fabula_id, *args, **kwargs):
        fabula_instance = self.get_object(fabula_id, request.user.id)
        if not fabula_instance:
            return Response(
                {"res": "Object with fabula id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = FabulaSerializer(fabula_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, fabula_id, *args, **kwargs):
        fabula_instance = self.get_object(fabula_id, request.user.id)
        if not fabula_instance:
            return Response(
                {"res": "Object with fabula id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'titulus': request.data.get('titulus'),
            'contentus': request.data.get('contentus'),
            'user': request.user.id,
        }
        serializer = FabulaSerializer(
            instance=fabula_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, fabula_id, *args, **kwargs):
        fabula_instance = self.get_object(fabula_id, request.user.id)
        if not fabula_instance:
            return Response(
                {"res": "Object with fabula id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        fabula_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
