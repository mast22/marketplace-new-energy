var person_select = document.getElementById('id_person');
var role_select = document.getElementById('id_role');

var permission_upload = document.getElementById('id_permission');
var staff_upload = document.getElementById('id_staff');
var equip_upload = document.getElementById('id_equip');
var exp_upload = document.getElementById('id_exp');
var reviews_upload = document.getElementById('id_reviews');
var entity_name = document.getElementById('id_entity_name')

var remove_option_from_select = function (select, option_value) {
    for (var i = 0; i < select.length; i++) {
        if (select.options[i].value == option_value) {
            select.remove(i);
        }
    }
};

var roleChange = function () {
    // Физ. лицо не может быть подрядчиком
    if (role_select.value == 'contractor') {
        permission_upload.disabled = false;
        staff_upload.disabled = false;
        equip_upload.disabled = false;
        exp_upload.disabled = false;
        reviews_upload.disabled = false;
        person_select.disabled = true;
        entity_name.disabled = false;
        person_select.value = 'entity';
    }
    if (role_select.value == 'custome' || !role_select.value){
        permission_upload.disabled = true;
        staff_upload.disabled = true;
        equip_upload.disabled = true;
        exp_upload.disabled = true;
        reviews_upload.disabled = true;
        entity_name.disabled = true;
        person_select.disabled = false;
    }
};

remove_option_from_select(role_select, 'staff');