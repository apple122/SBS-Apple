
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db.models import Prefetch
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .services_change_password import ChangePasswordSerializer
from .services_update_profile import UpdateUserSerializer
from rest_framework.permissions import IsAuthenticated
from .user_update_profile import UpdateUserProfileSerializer


STAFF = "is_staff"
is_staff = openapi.Parameter(STAFF, openapi.IN_QUERY,
                             description="fetch user or staff",
                             type=openapi.TYPE_BOOLEAN)

boolean_mapping = {
    "true": True,
    "false": False
}


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class ListUserView(ListAPIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(manual_parameters=[is_staff])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.all()
        queryset = self.get_is_staff(queryset)

        return queryset

    def get_is_staff(self, queryset):
        is_staff_query = self.request.query_params.get(STAFF)
        if (is_staff_query is None):
            return queryset
        is_staff = boolean_mapping[is_staff_query]

        if is_staff is not None:
            queryset = queryset.filter(is_staff=is_staff)
        return queryset


class RetrieveUserView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='refresh_token'),

        }
    ))
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class UpdateUserProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer
