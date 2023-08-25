from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
# Create your views here.

class login(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        username=request.data.get('username','')
        password=request.data.get('password','')
        if  username and password:
            if not User.objects.filter(username=username):
                return Response("username is wrong!!!")
            user = authenticate(username=username, password=password)
            if not user:
                return Response("password is wrong!!!")
            refresh=RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response("username or password field was not given!!")