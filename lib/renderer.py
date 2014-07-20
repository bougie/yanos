from django.shortcuts import render_to_response
from django.template import RequestContext


def request_render(request, template_name, template_vars):
    return render_to_response(
        template_name,
        template_vars,
        context_instance=RequestContext(request))
