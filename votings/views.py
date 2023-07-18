from django.shortcuts import render, redirect
from datetime import datetime
from .models import Voting


voted_list = {}


def votings_page(request):
    if not request.session or not request.session.session_key:
        request.session.save()

    votings = Voting.objects.all()
    for voting in votings:
        check_expired(voting)

    context = {
        'votings': votings,
    }

    return render(request, 'votings/index.html', context)


def add_vote(request, pk, character):
    if request.session.get('voted_list'):
        if str(pk) in request.session.get('voted_list'):
            return redirect('/votings')

    voting = Voting.objects.get(id=pk)
    if voting.expired:
        return redirect('/votings')

    setattr(voting, character, getattr(voting, character) + 1)
    voting.save()

    if pk not in voted_list:
        voted_list[pk] = character
        request.session['voted_list'] = voted_list

    return redirect('/votings')


def check_expired(voting):
    if datetime.now() >= voting.end_date.replace(tzinfo=None):
        voting.expired = True
    elif voting.max_votes:
        if voting.first_char_votes >= voting.max_votes \
                or voting.second_char_votes >= voting.max_votes:
            voting.expired = True
    else:
        voting.expired = False

    voting.save()
