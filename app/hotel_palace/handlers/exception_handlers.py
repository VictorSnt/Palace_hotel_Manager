from django.http import HttpResponse


def exception_handler(request, exc):
    return HttpResponse(exc, status=exc.code)
    