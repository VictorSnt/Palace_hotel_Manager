from django.http import HttpResponse

def exception_handler(request, exc):
    response = HttpResponse(exc, status=exc.code)
    response['Content-Type'] = 'application/json'
    return response
