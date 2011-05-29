from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Vote
from forms import VoteForm


# Public views

def index(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('done'))
    else:
        form = VoteForm()
    return render_to_response('index.html', {
            'form': form,
        }, context_instance=RequestContext(request))


def done(request):
    return render_to_response('done.html', {},
            context_instance=RequestContext(request))


# Staff views

@login_required
def staff(request):
    total = Vote.objects.count()
    yes = Vote.objects.filter(vote='Y').count()
    no = Vote.objects.filter(vote='N').count()
    return render_to_response('staff.html', {
        'no': no,
        'yes': yes,
        'total': total
        }, context_instance=RequestContext(request))


@login_required
def voters(request):
    voters = Vote.objects.order_by('last_name', 'first_name').all()
    return render_to_response('voters.html', {
        'voters': voters
        }, context_instance=RequestContext(request))
