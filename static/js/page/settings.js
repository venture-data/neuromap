var QEEGReport = function () {
    var handleValidation = function () {
        let superAdminForm = $('#add-super-admin');

        if (superAdminForm.length) {
            superAdminForm.validate({
                 ignore: [],
                 errorClass: 'field-error',
                 errorElement: 'span',
                 rules: {
                     name: {
                         required: true,
                     },
                     email: {
                         required: true,
                         email: true
                     },
                     password: {
                         required: true,
                     }
                 },
                 messages: {
                     name: {
                         required: "Please enter name."
                     },
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

            let userForm = $('#add-user');

            if (userForm.length) {
                userForm.validate({
                      ignore: [],
                      errorClass: 'field-error',
                      errorElement: 'span',
                      rules: {
                          name: {
                              required: true,
                          },
                          email: {
                              required: true,
                              email: true
                          },
                          password: {
                              required: true,
                          },
                          'permissions[]': {
                              required: true
                          }
                      },
                      messages: {
                          name: {
                              required: "Please enter name."
                          },
                          email: {
                              required: "Please enter email address.",
                              email: "Please enter valid email address."
                          },
                          password: {
                              required: "Please enter password."
                          },
                          'permissions[]': {
                              required: "Please select permission."
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
    }

    return {
        init: function () {
            handleValidation();
        }
    };
}();

$(document).ready(function () {
    QEEGReport.init();
});
