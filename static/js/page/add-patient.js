var AddPatient = function () {
    var handleValidation = function () {
        let patientForm = $('#add-patient');

        if (patientForm.length) {
            patientForm.validate({
                 ignore: [],
                 errorClass: 'field-error',
                 errorElement: 'span',
                 rules: {
                     name: {
                         required: true,
                     },
                     dob: {
                         required: true,
                     },
                     gender: {
                         required: true,
                     },
                     clinic_id: {
                         required: true,
                     },
                     contact_name: {
                         required: true,
                     },
                     contact_mobile: {
                         required: true,
                     }
                 },
                 messages: {
                     name: {
                         required: "Please enter name."
                     },
                     dob: {
                         required: "Please select DOB.",
                     },
                     gender: {
                         required: "Please select gender.",
                     },
                     clinic_id: {
                         required: "Please enter clinic ID.",
                     },
                     contact_name: {
                         required: "Please enter contact name.",
                     },
                     contact_mobile: {
                         required: "Please enter contact mobile number.",
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

        $('.datepicker').change(function() {
            var dob = $(this).val().split('/');
            $('#age').val(calculateAge(dob[2]+"/"+dob[1]+"/"+dob[0]));
        })
    }

    var allowNumberOnly = function () {
        $('.numberonly').keypress(function (e) {

            var charCode = (e.which) ? e.which : event.keyCode

            if (String.fromCharCode(charCode).match(/[^0-9]/g))

                return false;

        });
    }

    var calculateAge = function(dateString) {
        var today = new Date();
        var birthDate = new Date(dateString);
        var age = today.getFullYear() - birthDate.getFullYear();
        var m = today.getMonth() - birthDate.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }

        return age < 0 ? 0 : age;
    }

    return {
        init: function () {
            handleValidation();
            allowNumberOnly();
        }
    };
}();

$(document).ready(function () {
    AddPatient.init();
});
