from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import VoteForm


def index(request):
    """
    Only public view
    """
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
    return render_to_response('done.html', {})
