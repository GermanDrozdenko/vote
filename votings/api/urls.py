from django.urls import path
from .views import VotingView, VotingsView, VotingCharactersView, \
    VotingsWinnersView, VotingWinnerView, AddVoteView


urlpatterns = [
    path('votings/', VotingsView.as_view()),
    path('voting/<int:pk>', VotingView.as_view()),
    path('voting/<int:pk>/characters', VotingCharactersView.as_view()),
    path('votings/winners', VotingsWinnersView.as_view()),
    path('voting/<int:pk>/winner', VotingWinnerView.as_view()),
    path('voting/<int:pk>/add_vote', AddVoteView.as_view()),
]
