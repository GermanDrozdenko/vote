from django.shortcuts import render, redirect
from .models import Voting


def votings_page(request):
    votings = Voting.objects.all()
    context = {
        'votings': votings,
    }

    return render(request, 'votings/index.html', context)


def add_vote(request, pk, character):
    voting = Voting.objects.get(id=pk)
    setattr(voting, character, getattr(voting, character) + 1)
    voting.save()

    return redirect('/votings')
