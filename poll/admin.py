from django.contrib import admin
from models import Vote, Switch


class VoteAdmin(admin.ModelAdmin):
    exclude = ('vote',)


admin.site.register(Vote, VoteAdmin)
admin.site.register(Switch)
