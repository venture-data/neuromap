var Login = function () {
    var handleValidation = function () {
        let loginForm = $('#login');

        if (loginForm.length) {
            loginForm.validate({
                 ignore: [],
                 errorClass: 'field-error',
                 errorElement: 'span',
                 rules: {
                     email: {
                         required: true,
                         email: true
                     },
                     password: {
                         required: true,
                     }
                 },
                 messages: {
                     email: {
                         required: "Please enter email address.",
                         email: "Please enter valid email address."
                     },
                     password: {
                         required: "Please enter password."
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
    Login.init();
});
