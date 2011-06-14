import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Vote, Switch
from forms import VoteForm


def _is_active():
    s = get_object_or_404(Switch, pk=1)
    return s.vote_active


# Public views

def index(request):
    if not _is_active():
        return render_to_response('over.html', {},
            context_instance=RequestContext(request))
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
    votes = Vote.objects.all().filter(is_member=True, duplicate=False, deleted=False)
    total = votes.count()
    yes = votes.filter(vote='Y').count()
    no = votes.filter(vote='N').count()

    try:
        yes_p = yes * 100 / total
        no_p = no * 100 / total
    except ZeroDivisionError:
        yes_p = 0
        no_p = 0
    return render_to_response('staff.html', {
        'no': no,
        'yes': yes,
        'yes_p': yes_p,
        'no_p': no_p,
        'total': total
        }, context_instance=RequestContext(request))


@login_required
def voters(request):
    voters = Vote.objects.order_by('last_name', 'first_name').all()
    return render_to_response('voters.html', {
        'voters': voters
        }, context_instance=RequestContext(request))


@login_required
def ajax(request):
    res = {}
    allowed_actions = ['no-member', 'duplicate', 'delete']
    action = request.GET.get('action', None)
    uid = request.GET.get('uid', None)
    if not action:
        res['status'] = 'fail'
        res['message'] = "Missing action"
        return HttpResponse(json.dumps(res))
    if not uid:
        res['status'] = 'fail'
        res['message'] = "Missing uid"
        return HttpResponse(json.dumps(res))
    if action not in allowed_actions:
        res['status'] = 'fail'
        res['message'] = "Action forbidden"
        return HttpResponse(json.dumps(res))
    try:
        vote = Vote.objects.get(pk=uid)
    except:
        res['status'] = 'fail'
        res['message'] = "Resource not found"
        return HttpResponse(json.dumps(res))

    # Enough of security, let's get to work
    if action == 'no-member':
        vote.is_member = False
        vote.save()
    elif action == 'duplicate':
        vote.duplicate = True
        vote.save()
    elif action == 'delete':
        vote.deleted = True
        vote.save()
    else:
        pass

    res['status'] = 'success'

    return HttpResponse(json.dumps(res))


@login_required
def export(request):
    voters = Vote.objects.order_by('last_name', 'first_name').all()
    res = []
    for v in voters:
        res.append({
            'first': v.first_name,
            'last': v.last_name
        })
    return HttpResponse(json.dumps(res), mimetype='application/json')
