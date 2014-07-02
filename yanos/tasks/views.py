from flask import current_app, render_template, redirect, url_for, jsonify, request

from . import bp
from .forms import PriorityForm
from .core.priority import corePriorityAdd, corePriorityDelete, corePriorityEdit, corePriorityList

@bp.route('/tasks')
def index():
	tpl_vars = {
		'page_title': '\_o&lt;~ KOIN KOIN TASKS'
	}
	return render_template('tasks/index.j2', **tpl_vars)

# URL used to list and/or add a priority
@bp.route('/tasks/priority', methods=['GET', 'POST'])
# URL used to edit or delete (with ?delete=1) a priority
@bp.route('/tasks/priority/<int:pid>', methods=['POST'])
def priority(pid=None):
	form = PriorityForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			try:
				# Add (default behaviour) a priority
				if pid is None:
					corePriorityAdd(name=form.name.data)
				# Edit or delete a priority
				else:
					if 'delete' in request.args:
						if int(request.args.get('delete')) == 1:
							corePriorityDelete(id=pid)
						else:
							raise Exception('Bad value for delete')
					else:
						corePriorityEdit(id=pid, name=form.name.data)
			except Exception as e:
				current_app.logger.error(str(e))
				json = {
					'success': False
				}
			else:
				json = {
					'success': True
				}
		else:
			current_app.logger.error(form.errors)
			json = {
				'success': False
			}

		if request.is_xhr:
			return jsonify(**json)
		else:
			return redirect(url_for('tasks.priority'))
	else:
		try:
			priorities = corePriorityList()
		except Exception as e:
			current_app.logger.error(str(e))
			priorities = []

		tpl_vars = {
			'page_title': '\_o&lt;~ KOIN KOIN PRIORITY',
			'form': form,
			'priorities': priorities
		}
		return render_template('tasks/priority/index.j2', **tpl_vars)
