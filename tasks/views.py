from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from lib.renderer import request_render
from lib.response import JsonResponse
from .core.priority import corePriorityAdd, corePriorityEdit, \
    corePriorityDelete, corePriorityList
from .forms import PriorityForm


# @bp.route('/tasks')
def index(request):
    tpl_vars = {
        'page_title': '\_o<~ KOIN KOIN TASKS'
    }
    return request_render(request, 'tasks/index.j2', tpl_vars)


# URL used to list and/or add a priority
# @bp.route('/tasks/priority', methods=['GET', 'POST'])
# URL used to edit or delete (with ?delete=1) a priority
# @bp.route('/tasks/priority/<int:pid>', methods=['POST'])
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
                    'success': False
                }
            else:
                json = {
                    'success': True
                }
        else:
            json = {
                'success': False
            }

        if request.is_ajax():
            return JsonResponse(json)
        else:
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
