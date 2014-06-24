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
		redirect(data.recdirect);
	} else {
		// Show error message before the login form
		$('#login-popup .modal-body').prepend(
			'<div class="modal-notif">' + data.msg + '</div>'
		);
	}
}

$(function() {
	$('#register-popup').on('shown.bs.modal', function() {
		// Display the register form if it was previously hide
		// (like after a succes form submission)
		$('#register-popup .modal-body form').show();

		// Show form cancel and valid buttons
		var confirm_buttons = '<div class="modal-footer">';
		confirm_buttons += '<button type="button" class="btn btn-default" data-dismiss="modal">Annuler</button>';
		confirm_buttons += '<button type="button" class="btn btn-primary" id="btn-submit">Valider</button>';
		confirm_buttons += '</div>';
		$('#register-popup .modal-content').append(confirm_buttons);

		// Send the form by ajax request
		$('#register-popup #btn-submit').on('click', function() {

			var action = $('#register-popup #register-form').attr('action');
			var pwd1 = $('#register-popup #register-form #password').val();
			var pwd2 = $('#register-popup #register-form #password2').val();

			if(pwd1 == pwd2) {
				$.ajax({
					url: action,
					type: 'POST',
					dataType: 'json',
					data: $('form#register-form').serialize(),
					success: register_response_handler
				});
			}
		});
	});
	$('#register-popup').on('hidden.bs.modal', function() {
		// Remove custom header and custom footer
		// Default one will be reloaded for the next showing of the modal
		if($('#register-popup .modal-notif')) {
			$('#register-popup .modal-notif').remove();
		}
		if($('#register-popup .modal-footer')) {
			$('#register-popup .modal-footer').remove();
		}
	});
	$('#login-popup').on('shown.bs.modal', function() {
		// Display the login form if it was previously hide
		// (like after a succes form submission)
		$('#login-popup .modal-body form').show();

		// Show form cancel and valid buttons
		var confirm_buttons = '<div class="modal-footer">';
		confirm_buttons += '<button type="button" class="btn btn-default" data-dismiss="modal">Annuler</button>';
		confirm_buttons += '<button type="button" class="btn btn-primary" id="btn-submit">Valider</button>';
		confirm_buttons += '</div>';
		$('#login-popup .modal-content').append(confirm_buttons);

		// Send the form by ajax request
		$('#login-popup #btn-submit').on('click', function() {

			var action = $('#login-popup #login-form').attr('action');

			if(pwd1 == pwd2) {
				$.ajax({
					url: action,
					type: 'POST',
					dataType: 'json',
					data: $('form#login-form').serialize(),
					success: login_response_handler
				});
			}
		});
	});
})
