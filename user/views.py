from rest_framework.exceptions import AuthenticationFailed, ValidationError, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False)
    def login(self, request):
        if 'email' not in request.data:
            data = {'email': 'Email must be provided'}
            if 'password' not in request.data:
                data['password'] = ['Password must be provided']
            raise ValidationError(data)
        if 'password' not in request.data:
            raise ValidationError({'password': ['Password must be provided']})

        try:
            user = User.objects.get(email=request.data.get('email'))
        except User.DoesNotExist:
            raise NotFound({'message': 'User with provided credentials does not exist'})

        if not user.check_password(request.data.get('password')):
            raise AuthenticationFailed({'message': 'Incorrect password'})

        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)
        response = Response()
        response.set_cookie('refresh', str(refresh))
        response.data = {'access': str(refresh.access_token)}
        return response

    @action(methods=['GET'], detail=False,
            permission_classes=[IsAuthenticated])
    def user(self, request):
        user = request.user
        data = UserSerializer(user).data
        return Response(data)

    @action(detail=True, methods=['POST'], url_path='change_password')
    def change_password(self, request, pk=None):
        if 'new_password' not in request.data:
            raise ValidationError({'new_password': 'Password must be provided'})

        password = request.data['new_password']
        user = User.objects.get(id=pk)
        user.set_password(password)
        user.save()
        return Response({'status': 'password changed'})
