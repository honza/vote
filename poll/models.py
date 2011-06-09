from datetime import datetime
from django.db import models

CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No')
)

class Vote(models.Model):
    added = models.DateTimeField(default=datetime.now)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    vote = models.CharField(max_length=1, choices=CHOICES)
    is_member = models.BooleanField(default=True)
    duplicate = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s, %s" % (self.last_name, self.first_name)


class Switch(models.Model):
    vote_active = models.BooleanField(default=True)

    def __unicode__(self):
        if self.vote_active:
            return "The vote is on."
        else:
            return "The vote is off."

