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

var control_entity_features = function() {
    // Триггер для контроля полей юр. лица
    permission_upload.disabled = false;
    staff_upload.disabled = false;
    equip_upload.disabled = false;
    exp_upload.disabled = false;
    reviews_upload.disabled = false;
    entity_name.disabled = false;
};

var remove_control_entity_features = function() {
    person_select.value = '';
    person_select.disabled = false;
};

var control_individual_features = function() {
    // Триггер для контроля полей физ. лица
    permission_upload.disabled = true;
    staff_upload.disabled = true;
    equip_upload.disabled = true;
    exp_upload.disabled = true;
    reviews_upload.disabled = true;
    entity_name.disabled = true;
    person_select.disabled = false;
};

var roleChange = function() {
    // Физ. лицо не может быть подрядчиком
    if (role_select.value == 'contractor') {
        // Подрядчик может быть только юр. лицом
        person_select.value = 'entity';
        person_select.disabled = true;
        control_entity_features();
    }
    if (role_select.value == 'custome') {
        // убираем запреты
        remove_control_entity_features();
        // TODO Убрать инпуты для заявителя юр. лица
    }
    if (!role_select.value) {
        // В случае если выбирается "---------", то вырубаем всё
        control_entity_features();
        // TODO придумай что нибудь
    }
};

var personChange = function() {
    // Юр. лицо всегда должно вводить своё название
    if (person_select.value == 'individual') {
        control_individual_features();
    }
    if (person_select.value == 'entity') {
        control_entity_features();
    }
    if (!person_select.value) {
        control_entity_features();
        // TODO аналог 52 строчки, чёнить надо сделать
    }
};

// TODO Удалить из формы на backend
remove_option_from_select(role_select, 'staff');