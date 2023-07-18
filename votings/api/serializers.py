from rest_framework import serializers
from votings.models import Voting
from characters.models import Character


class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        exclude = ('img_url', )
