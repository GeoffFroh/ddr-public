import logging
logger = logging.getLogger(__name__)

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import Http404, get_object_or_404, render_to_response
from django.template import RequestContext

from ui.models import Repository, Organization, Collection, Entity, File


# views ----------------------------------------------------------------

def detail( request, repo, org, cid, eid, role, sha1 ):
    ffile = File.get(repo, org, cid, eid, role, sha1)
    if not ffile:
        raise Http404
    return render_to_response(
        'ui/files/detail.html',
        {
            'repo': repo,
            'org': org,
            'cid': cid,
            'eid': eid,
            'role': role,
            'sha1': sha1,
            'object': ffile,
        },
        context_instance=RequestContext(request, processors=[])
    )
