from django.contrib import admin
from models import Vote


class VoteAdmin(admin.ModelAdmin):
    exclude = ('vote',)


admin.site.register(Vote, VoteAdmin)
