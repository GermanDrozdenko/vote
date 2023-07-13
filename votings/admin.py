from django.contrib import admin
from .models import Voting


class VotingAdmin(admin.ModelAdmin):
    exclude = ('expired', 'first_char_votes', 'second_char_votes')


admin.site.register(Voting, VotingAdmin)
