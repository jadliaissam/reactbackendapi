from django.http import JsonResponse
from reactbackapp.models import MyUser, Product, Operation
from rest_framework import viewsets
from rest_framework import permissions
from reactbackapp.serializers import UserSerializer, ProductSerializer, OperationSerializer


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


def api_home(request):
    return JsonResponse(data={'message': "Welcome To JADLI AISSAM's Backend Demo App !"})

