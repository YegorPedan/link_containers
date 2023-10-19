from rest_framework import viewsets, status
from rest_framework.response import Response


class TestController(viewsets.ViewSet):
    serializer_classes = {
        "get_result": None,
    }

    def get_result(self, request):
        return Response(data={"result": "python-test-api"}, status=status.HTTP_200_OK)


class EventController(viewsets.ViewSet):
    serializer_classes = {
        "get_result": None,
    }

    def get_result(self, request):
        return Response(data={"result": "python-test-api"}, status=status.HTTP_200_OK)
