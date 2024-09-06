var ForgotPassword = function () {
    var handleValidation = function () {
        let forgotPasswordForm = $('#forgot-password');

        if (forgotPasswordForm.length) {
            forgotPasswordForm.validate({
                 ignore: [],
                 errorClass: 'field-error',
                 errorElement: 'span',
                 rules: {
                     email: {
                         required: true,
                         email: true
                     }
                 },
                 messages: {
                     email: {
                         required: "Please enter email address.",
                         email: "Please enter valid email address."
                     }
                 },
                 errorPlacement: function (error, element) {
                     if (element.attr("data-error-container")) {
                         error.appendTo('#' + element.attr("data-error-container"));
                     } else {
                         error.insertAfter(element);
                     }
                 }
             });
        }
    }

    return {
        init: function () {
            handleValidation();
        }
    };
}();

$(document).ready(function () {
    ForgotPassword.init();
});
