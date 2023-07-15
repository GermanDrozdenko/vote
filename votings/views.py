from django.shortcuts import render, redirect
from datetime import datetime
from .models import Voting


def votings_page(request):
    votings = Voting.objects.all()
    for voting in votings:
        if datetime.now() >= voting.end_date.replace(tzinfo=None):
            voting.expired = True
        elif voting.first_char_votes >= voting.max_votes \
                or voting.second_char_votes >= voting.max_votes:
            voting.expired = True
        else:
            voting.expired = False

    context = {
        'votings': votings,
    }

    return render(request, 'votings/index.html', context)


def add_vote(request, pk, character):
    voting = Voting.objects.get(id=pk)
    setattr(voting, character, getattr(voting, character) + 1)
    voting.save()

    return redirect('/votings')
