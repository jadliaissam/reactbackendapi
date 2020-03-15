from django.http import JsonResponse


def home(request):
    return JsonResponse(data={'message': "Welcome To JADLI AISSAM's Backend Demo App !"})