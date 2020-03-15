from django.http import JsonResponse
from reactbackapp.models import MyUser, Product, Operation
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from reactbackapp.serializers import UserSerializer, ProductSerializer, OperationSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  #IsAuthenticated]


class OperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    permission_classes = [permissions.AllowAny]  #IsAuthenticated]


class Home(APIView):
    def get(self, request):
        return Response({'message': "Welcome To JADLI AISSAM's Backend Demo App !"})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = MyUser.objects.filter(username=username, password=password)
        if users:
            return JsonResponse(status=200, data={'token': users[0].token})
        else:
            return JsonResponse(status=401, data={'error': 'Authentication Failed'})
    else:
        return JsonResponse(status=403, data={'error': 'Not Allowed'})


def logout(request):
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        users = MyUser.objects.filter(token=token)
        if users:
            return JsonResponse(status=200, data={'success': 'Sucessfully Logged out'})
        else:
            return JsonResponse(status=401, data={'error': 'Authentication Failed'})
    else:
        return JsonResponse(status=403, data={'error': 'Not Allowed'})