import logging
logger = logging.getLogger(__name__)

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import Http404, get_object_or_404, render_to_response
from django.template import RequestContext


# views ----------------------------------------------------------------

def index( request ):
    return render_to_response(
        'ui/index.html',
        {},
        context_instance=RequestContext(request, processors=[])
    )

def cite( request ):
    return render_to_response(
        'ui/cite.html',
        {},
        context_instance=RequestContext(request, processors=[])
    )
