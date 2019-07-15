var role_select = $('#id_role');
var person_select = $('#id_person');

var permission_upload = $('#id_permission');
var staff_upload = $('#id_staff');
var equip_upload = $('#id_equip');
var exp_upload = $('#id_exp');
var reviews_upload = $('#id_reviews');

var entity_name = $('#id_entity_name');

var exp_upload = [permission_upload, staff_upload, equip_upload, exp_upload, reviews_upload];

// Убираем значение staff, TODO добавить валидацию на server-side
$('#id_role option[value="staff"]').remove();

// TODO добавить DRY

var roleChange = function() {
    // Вырубаем опыт, вырубаем юр лицо

    if (role_select.val() == 'custome') {
        exp_upload.forEach(element => {
            element.prop("disabled", true);
        });

        person_select.val('').change();     // DRY
        person_select.prop("disabled", false);
    } else if (role_select.val() == 'contractor') {
        entity_name.prop("disabled", false);
        exp_upload.forEach(element => {
            element.prop("disabled", false);
        });
        // Подрядчик должен быть юр лицом.
        person_select.val("entity").change();
        person_select.prop("disabled", true);
    } else {
        // освобождаем от блокировки все поля
        entity_name.prop("disabled", false);
        exp_upload.forEach(element => {
            element.prop("disabled", false);
        });
        person_select.val('').change();     // DRY
        person_select.prop("disabled", false);
    }
};

var personChange = function() {
    if (person_select.val() == 'entity') {
        // продолжить тут
        entity_name.prop("disabled", false);
    } else if (person_select.val() == 'individual') {
        // Очищаем и блокируем поле ввода имени юр. лица
        entity_name.val('');
        entity_name.prop("disabled", true);
    } else {
        entity_name.prop("disabled", false);
    }
};
