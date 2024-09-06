var QEEGReport = function () {
    var handleValidation = function () {
        let reportForm = $('#add-report');

        if (reportForm.length) {
            reportForm.validate({
                 ignore: [],
                 errorClass: 'field-error',
                 errorElement: 'span',
                 rules: {
                     recording_date: {
                         required: true,
                     },
                     edf_file: {
                         required: true,
                     },
                     report_type: {
                         required: true,
                     }
                 },
                 messages: {
                     recording_date: {
                         required: "Please select reporting date.",
                     },
                     edf_file: {
                         required: "Please select EDF file.",
                     },
                     report_type: {
                         required: "Please select report type.",
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
    QEEGReport.init();
});
