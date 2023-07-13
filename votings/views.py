from django.shortcuts import render
from .models import Voting


def votings_page(request):
    votings = Voting.objects.all()
    context = {
        'votings': votings,
    }

    return render(request, 'votings/index.html', context)
