from django.db import models
from characters.models import Character


class Voting(models.Model):
    title = models.CharField(max_length=60)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_votes = models.IntegerField(blank=True, null=True)
    expired = models.BooleanField(default=False)
    characters = models.ManyToManyField(Character, related_name='characters')
    first_char_votes = models.IntegerField(default=0)
    second_char_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
