from django.shortcuts import render
from .models import Character


def characters_page(request):
    context = {
        'characters': Character.objects.all(),
    }

    return render(request, 'characters/index.html', context)
