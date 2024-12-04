from django.contrib.auth import authenticate
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout
)

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer, UserProfileSerializer


class RegisterView(APIView):
    # 不进行身份校验，任何人都可以访问
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': '注册成功',
                'user': UserProfileSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response({'error': "用户名已经存在"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            # 生成token
            refresh = RefreshToken.for_user(user)

            return Response({
                'message': '登录成功',
                'user': UserProfileSerializer(user).data,
                'token': str(refresh.access_token),  # 返回token
            })
        return Response({'error': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        # 用户退出登录
        auth_logout(request)
        return Response({'message': '退出成功'}, status=status.HTTP_200_OK)
