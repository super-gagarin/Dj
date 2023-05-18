from django.shortcuts import redirect
from django.shortcuts import render


def redirect_view(request):
    response = redirect('/about/')
    return response


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
