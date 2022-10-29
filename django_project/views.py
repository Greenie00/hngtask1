from rest_framework.views import APIView
from django.http import JsonResponse


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "slackUsername":
            "Greenie",
            "backend":
            True,
            "age":
            20,
            "bio":
            "My name is George Barasinopre, I am lazy at everything else until it's time to debug"
        }

        return JsonResponse(data)
