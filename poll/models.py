from django.db import models

CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No')
)

class Vote(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    vote = models.CharField(max_length=1, choices=CHOICES)
    is_member = models.BooleanField(default=True)
    duplicate = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s, %s" % (self.last_name, self.first_name)
