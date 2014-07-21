from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from lib.renderer import request_render
from lib.response import JsonResponse
from .core.priority import corePriorityAdd, corePriorityEdit, \
    corePriorityDelete, corePriorityList
from .core.state import coreStateAdd, coreStateEdit, coreStateDelete, \
    coreStateList
from .forms import PriorityForm, StateForm


# @bp.route('/tasks')
def index(request):
    tpl_vars = {
        'page_title': '\_o<~ KOIN KOIN TASKS'
    }
    return request_render(request, 'tasks/index.j2', tpl_vars)


@login_required
def priority(request, pid=None):
    if request.method == 'POST':
        form = PriorityForm(request.POST)
        if form.is_valid():
            try:
                # Add (default behaviour) a priority
                if pid is None:
                    corePriorityAdd(name=form.cleaned_data['name'])
                # Edit or delete a priority
                else:
                    delete = request.GET.get('delete', None)
                    if delete is not None:
                        if int(delete) == 1:
                            corePriorityDelete(id=pid)
                        else:
                            raise Exception('Bad value for delete')
                    else:
                        corePriorityEdit(id=pid, name=form.cleaned_data['name'])
            except Exception:
                json = {
                    'success': False,
                    'msg': 'Impossible d\'effectuer l\'action demandée'
                }
            else:
                json = {
                    'success': True,
                    'msg': 'Action éffectuée avec success'
                }
        else:
            json = {
                'success': False,
                'msg': 'Données saisies invalides'
            }

        if request.is_ajax():
            return JsonResponse(json)
        else:
            if json['success']:
                messages.add_message(request, messages.SUCCESS, json['msg'])
            else:
                messages.add_message(request, messages.ERROR, json['msg'])

            return redirect('tasks_priority')
    else:
        try:
            priorities = corePriorityList()
        except Exception:
            priorities = []

        form = PriorityForm()
        tpl_vars = {
            'page_title': '\_o<~ KOIN KOIN PRIORITY',
            'form': form,
            'priorities': priorities
        }
        return request_render(request, 'tasks/priority/index.j2', tpl_vars)


@login_required
def state(request, sid=None):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            try:
                # Add (default behaviour) a state
                if sid is None:
                    coreStateAdd(name=form.cleaned_data['name'])
                # Edit or delete a state
                else:
                    delete = request.GET.get('delete', None)
                    if delete is not None:
                        if int(delete) == 1:
                            coreStateDelete(id=sid)
                        else:
                            raise Exception('Bad value for delete')
                    else:
                        coreStateEdit(id=sid, name=form.cleaned_data['name'])
            except Exception:
                json = {
                    'success': False,
                    'msg': 'Impossible d\'effectuer l\'action demandée'
                }
            else:
                json = {
                    'success': True,
                    'msg': 'Action éffectuée avec success'
                }
        else:
            json = {
                'success': False,
                'msg': 'Données saisies invalides'
            }

        if request.is_ajax():
            return JsonResponse(json)
        else:
            if json['success']:
                messages.add_message(request, messages.SUCCESS, json['msg'])
            else:
                messages.add_message(request, messages.ERROR, json['msg'])

            return redirect('tasks_state')
    else:
        try:
            states = coreStateList()
        except Exception:
            states = []

        form = StateForm()
        tpl_vars = {
            'page_title': '\_o<~ KOIN KOIN STATE',
            'form': form,
            'states': states
        }
        return request_render(request, 'tasks/state/index.j2', tpl_vars)
