function redirect(url) {
	window.location.replace(url);
}

function notification_message(msg, state) 
{
	var html = "";

	html += "<div id=\"jspopmessage\" class=\"pop pop-top-wide pop-" + state + "\">"
	html += "	<div class=\"pop-body\">" + msg + "</div>"
	html += "</div>"

	$('#content').prepend(html);
	$('#jspopmessage').pop('show', {'delay': 1500});
	$('#jspopmessage').on('pop.hidden', function() {
		$('#jspopmessage').remove();
	});
}

/**
 * Handle ajax response after form submit for the register form
 */
function register_response_handler(data) {
	if($('#register-popup .modal-notif')) {
		// Remove a notification message if it exists
		$('#register-popup .modal-notif').remove();
	}

	if(data.success) {
		// Hide an empty the register form
		$('#register-popup .modal-body form').hide();
		$('#register-popup .modal-body form input[type="text"]').val('');
		$('#register-popup .modal-body form input[type="password"]').val('');

		// Show the success notifcation
		$('#register-popup .modal-body').prepend(
			'<div class="modal-notif">' + data.msg + '</div>'
		);

		// Replace form buttons by a close one
		$('#register-popup .modal-footer').html(
			'<button type="button" class="btn btn-default" data-dismiss="modal">Fermer</button>'
		);
	} else {
		// Show error message before the register form
		$('#register-popup .modal-body').prepend(
			'<div class="modal-notif">' + data.msg + '</div>'
		);
	}
}

/**
 * Handle ajax response after form submit for the login form
 */
function login_response_handler(data) {
	if($('#login-popup .modal-notif')) {
		// Remove a notification message if it exists
		$('#login-popup .modal-notif').remove();
	}

	if(data.success) {
		if(data.redirect) {
			redirect(data.redirect);
		} else {
			notification_message(data.msg, 'success');
		}
	} else {
		// Show error message before the login form
		$('#login-popup .modal-body').prepend(
			'<div class="modal-notif">' + data.msg + '</div>'
		);
	}
}

/**
 * Function which will be called when clicking on the register button
 */
function register_click_callback() {
	var action = $(name + ' #register-form').attr('action');
	var pwd1 = $(name + ' #register-form #password').val();
	var pwd2 = $(name + ' #register-form #password2').val();

	if(pwd1 == pwd2) {
		$.ajax({
			url: action,
			type: 'POST',
			dataType: 'json',
			data: $('form#register-form').serialize(),
			success: register_response_handler
		});
	}
}

/**
 * Function which will be called when clicking on the login button
 */
function login_click_callback() {
	var action = $('#login-popup #login-form').attr('action');

	$.ajax({
		url: action,
		type: 'POST',
		dataType: 'json',
		data: $('form#login-form').serialize(),
		success: login_response_handler
	});
}

function set_form_modal(name, click_callback) {
	function set_basic_buttons(name) {
		// Show form cancel and valid buttons
		var confirm_buttons = '<div class="modal-footer">';
		confirm_buttons += '<button type="button" class="btn btn-default" data-dismiss="modal">Annuler</button>';
		confirm_buttons += '<button type="button" class="btn btn-primary" id="btn-submit">Valider</button>';
		confirm_buttons += '</div>';
		$(name + ' .modal-content').append(confirm_buttons);
	}

	$(name).on('loaded.bs.modal', function() {
		set_basic_buttons(name);
	});
	$(name).on('show.bs.modal', function() {
		// Display the form if it was previously hide
		// (like after a succes form submission)
		$(name + ' .modal-body form').show();
	});
	$(name).on('shown.bs.modal', function() {
		// Send the form by ajax request
		$(name + ' #btn-submit').on('click', click_callback);
	});
	$(name).on('hidden.bs.modal', function() {
		// Remove custom header and custom footer
		// Default one will be reloaded for the next showing of the modal
		if($(name + ' .modal-notif')) {
			$(name + ' .modal-notif').remove();
		}
		if($(name + ' .modal-footer')) {
			$(name + ' .modal-footer').remove();

			set_basic_buttons(name);
		}
	})
}

/*
 * Handle "request" to manage priority/state add and edit forms
 */
function edit_intable_handler(htmlid) {
	// Current item ID which is edited
	var curr_id = -1;
	// Current item name which is edited
	var curr_name = "";
	// Value of the td action cell before entering in "edit mode"
	var curr_act = "";

	/**
	 * Add input into the table to edit an item
	 */
	var show_input_fct = function() {
		// TR ligne of the table which contains the item
		var elt = $(this).parent();
		// item ID
		var id = elt.attr('id').split('-')[1];

		if(id != undefined && (curr_id == -1 || id == curr_id)) {
			var td_name_elt = elt.children('td:nth-child(1)');
			var td_act_elt = elt.children('td:nth-child(2)');

			// Save the current item * to (re)set it when discard changes
			curr_name = td_name_elt.html();
			curr_act = td_act_elt.html();
			curr_id = id;

			var input = "<input type=\"text\" class=\"form-control\" name=\"name\" value=\"" + curr_name + "\" />";
			var actions = "<button id=\"btn-send\" type=\"button\" class=\"btn btn-success btn-xs\">Valider</button>";
			actions += "<button id=\"btn-cancel\" type=\"button\" class=\"btn btn-warning btn-xs\">Annuler</button>";
			td_name_elt.html(input);
			td_act_elt.html(actions);

			// Remove click event listener -> can't edit another field
			$(htmlid + ' table tbody tr td:nth-child(1)').unbind('click');
			// Disable field editing when clicked on cancel button
			$(htmlid + ' #btn-cancel').on('click', hide_input_fct);
			$(htmlid + ' #btn-send').on('click', save_input_fct);
		}
	};
	/**
	 * Remove input in the table and only display item informations
	 */
	var hide_input_fct = function() {
		var elt = $('#lineid-' + curr_id);
		var td_name_elt = elt.children('td:nth-child(1)');
		var td_act_elt = elt.children('td:nth-child(2)');

		td_name_elt.html(curr_name);
		td_act_elt.html(curr_act);
		curr_name = "";
		curr_act = "";
		curr_id = -1;

		$(htmlid + ' table tbody tr td:nth-child(1)').on('click', show_input_fct);

		$(htmlid + ' #btn-delete').on('click', delete_intable_handler);
	};
	/**
	 * Send and save changes
	 */
	var save_input_fct = function() {
		var elt = $('#lineid-' + curr_id);
		var action = $(htmlid).attr('action') + '/' + curr_id;

		$.ajax({
			url: action,
			type: 'POST',
			dataType: 'json',
			data: $('form' + htmlid).serialize(),
			success: function (data) {
				if(data.success) {
					curr_name = $(htmlid + ' input[name=name]').val();
					hide_input_fct();

					notification_message(data.msg, 'success');
				}
			}
		});
	};

	$(htmlid + ' table tbody tr td:nth-child(1)').on('click', show_input_fct);
}
/**
 * Handle "requests" to delete a priority
 */
function delete_intable_handler() {
	var form = $(this).parents('form').first();
	var htmlid = '#' + form.attr('id');
	var action = form.attr('action');

	// Item ID
	var item_id = $(this).parent().parent().attr('id').split('-')[1];
	// Item name
	var item_name = $('#lineid-' + item_id).children('td:nth-child(1)').html();

	// Add a tmp input with the item name
	// It will be use for the form validation
	$(htmlid).prepend('<input type="hidden" id="name" name="name" value="' + item_name + '">');

	$.ajax({
		url: action + '/' + item_id + '?delete=1',
		type: 'POST',
		dataType: 'json',
		data: $('form' + htmlid).serialize(),
		success: function (data) {
			if(data.success) {
				// Remove table line of the priority
				$('#lineid-' + item_id).remove();

				notification_message(data.msg, 'success');
			}
		}
	});

	// Manually remove the input if we want to delete another priority
	// without refresh the page
	$(htmlid + ' #name').remove();
}

$(function() {
	set_form_modal('#register-popup', register_click_callback);
	set_form_modal('#login-popup', login_click_callback);

	$('#form-priority-edit #btn-delete').on('click', delete_intable_handler);
	edit_intable_handler('#form-priority-edit');

	$('#form-state-edit #btn-delete').on('click', delete_intable_handler);
	edit_intable_handler('#form-state-edit');
})
