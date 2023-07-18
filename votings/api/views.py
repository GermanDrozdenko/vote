from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VotingSerializer, CharacterSerializer
from votings.models import Voting
from votings.views import check_expired


class VotingsView(APIView):
    def get(self, request):
        try:
            votings = Voting.objects.all()
            for voting in votings:
                check_expired(voting)

            serializer = VotingSerializer(votings, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response('No voting exists')


class VotingView(APIView):
    def get(self, request, pk):
        try:
            voting = Voting.objects.get(id=pk)
            check_expired(voting)
            serializer = VotingSerializer(voting)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(f'Voting with ID {pk} does not exist')


class VotingCharactersView(APIView):
    def get(self, request, pk):
        try:
            voting = Voting.objects.get(id=pk)
            characters = voting.characters.all()
            serializer = CharacterSerializer(characters, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(f'Voting with ID {pk} does not exist')


class VotingsWinnersView(APIView):
    def get(self, request):
        votings = Voting.objects.all()
        for voting in votings:
            check_expired(voting)

        winners_list = []

        try:
            votings = votings.filter(expired=True)
            for voting in votings:
                if voting.first_char_votes > voting.second_char_votes:
                    character = voting.characters.first()
                    winner = add_winner(voting, character)
                    winners_list.append(winner)
                elif voting.second_char_votes > voting.first_char_votes:
                    character = voting.characters.last()
                    winner = add_winner(voting, character)
                    winners_list.append(winner)
                else:
                    winner = add_draw(voting)
                    winners_list.append(winner)

            return Response(winners_list)
        except ObjectDoesNotExist:
            return Response('No expired voting exists')


class VotingWinnerView(APIView):
    def get(self, request, pk):
        try:
            voting = Voting.objects.get(id=pk)
            check_expired(voting)
            if not voting.expired:
                return Response(f'Voting with ID {pk} is active')

            if voting.first_char_votes > voting.second_char_votes:
                character = voting.characters.first()
                winner = add_winner(voting, character)
            elif voting.second_char_votes > voting.first_char_votes:
                character = voting.characters.last()
                winner = add_winner(voting, character)
            else:
                winner = add_draw(voting)

            return Response(winner)
        except ObjectDoesNotExist:
            return Response(f'Voting with ID {pk} does not exist')


class AddVoteView(APIView):
    voted_list = {}

    def post(self, request, pk):
        if request.session.get('voted_list'):
            if str(pk) in request.session.get('voted_list'):
                return Response('You already voted')

        data = JSONParser().parse(request)
        character = data.get('character')

        try:
            voting = Voting.objects.get(id=pk)
            if voting.expired:
                return Response(f'Voting with ID {pk} is expired')
        except ObjectDoesNotExist:
            return Response(f'Voting with ID {pk} does not exist')

        if character == 1:
            voting.first_char_votes += 1
        elif character == 2:
            voting.second_char_votes += 1
        else:
            return Response('Incorrect JSON input, provide "character" key with 1 or 2 value')

        voting.save()

        if pk not in AddVoteView.voted_list:
            AddVoteView.voted_list[pk] = character
            request.session['voted_list'] = AddVoteView.voted_list

        if request.session.get('voted_list'):
            if str(pk) in request.session.get('voted_list'):
                return Response('You already voted')

        return Response('Vote accepted')


def add_winner(voting, character):
    winner = {
        'voting_id': voting.id,
        'voting_title': voting.title,
        'winner_id': character.id,
        'first_name': character.first_name,
        'second_name': character.second_name,
        'last_name': character.last_name,
    }

    return winner


def add_draw(voting):
    draw = {
        'voting_id': voting.id,
        'voting_title': voting.title,
        'winner_id': None,
    }

    return draw
