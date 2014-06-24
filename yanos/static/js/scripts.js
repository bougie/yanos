function redirect(url) {
	window.location.replace(url);
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

$(function() {
	set_form_modal('#register-popup', register_click_callback);
	set_form_modal('#login-popup', login_click_callback);
})
