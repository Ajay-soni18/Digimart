from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(["GET"])
def health_check(request: Request) -> Response:
    """Liveness probe: confirms the API process is up and serving requests."""
    return Response({"status": "ok"})
