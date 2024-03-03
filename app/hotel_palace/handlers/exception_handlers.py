from django.http import HttpResponse


def validation_exception(request, exc):
    return HttpResponse(exc, status=exc.code)
    