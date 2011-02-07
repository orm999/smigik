var gAnimationSpeed = "fast";
var gAnimationSpeedSlow = "slow";
var gShowNoticeTime = 2000;
var gRequestDelay = 1000;

$.clear_form_elements = function clear_form_elements(element) {
    $(element).find(':input').each(function() {
        switch(this.type) {
            case 'password':
            case 'select-multiple':
            case 'select-one':
            case 'text':
            case 'textarea':
            case 'file':
                $(this).val('');
                break;
            case 'checkbox':
            case 'radio':
                this.checked = false;
        }
    });
}

$(document).ready(function() {
})
