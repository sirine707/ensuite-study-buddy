from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<h1>Welcome to Ensuite Study Buddy!</h1><p>This is the homepage.</p>"
    )
