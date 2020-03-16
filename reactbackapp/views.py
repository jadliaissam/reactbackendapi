from django.http import JsonResponse
from reactbackapp.models import MyUser, Product, Operation
from rest_framework import viewsets
from rest_framework import permissions
from reactbackapp.serializers import UserSerializer, ProductSerializer, OperationSerializer
from django.conf import settings

api_permission = None
if settings.AUTH_API:
    api_permission = permissions.IsAuthenticated
else:
    api_permission = permissions.AllowAny


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [api_permission]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [api_permission]


class OperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    permission_classes = [api_permission]


def api_home(request):
    return JsonResponse(data={'message': "Welcome To JADLI AISSAM's Backend Demo App !"})

