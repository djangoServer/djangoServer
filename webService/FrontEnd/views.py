from django.shortcuts import render


def Page(request):
    return render(request, 'Page/index.html', {})

# Create your views here.
