from django.forms import ModelForm, ChoiceField, ValidationError
from models import Vote


class VoteForm(ModelForm):

    vote = ChoiceField

    class Meta:
        model = Vote
        exclude = ('added', 'deleted', 'duplicate', 'is_member',)

    def clean(self):
        data = self.cleaned_data
        first = data['first_name'].strip()
        last = data['last_name'].strip()

        if not first:
            raise ValidationError("Please enter a valid first name.")
        if not last:
            raise ValidationError("Please enter a valid last name.")

        data['first_name'] = first
        data['last_name'] = last

        return data
