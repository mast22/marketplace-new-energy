from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestProjectAuth(StaticLiveServerTestCase):

    # Конфигурация драйвера
    opts = Options()
    opts.headless = True

    def setUp(self):
        self.browser = Firefox(options=self.opts)

    def tearDown(self):
        self.browser.close()

    def test_register_user(self):
        self.browser.get(self.live_server_url)

        # тестируем регистрацию и форму регистрации

        email = 'testtest@testtest.ru'
        password = 'testtestpassword123'

        register_user_url = self.live_server_url + reverse('account_signup')
        self.browser.get(register_user_url)

        email_input = self.browser.find_element_by_id('id_email')
        email_input.send_keys(email)

        password_input = self.browser.find_element_by_id('id_password1')
        password_input.send_keys(password)

        submit_input = self.browser.find_element_by_tag_name('button')
        submit_input.click()

        # После регистрации необходимо заполнить информацию

        role_register_url = self.live_server_url + \
            reverse('users:role_register')
        self.browser.get(role_register_url)

        # Выбираем роль заявителя

        role_input = Select(self.browser.find_element_by_id('id_role'))
        role_input.select_by_value('contractor')

        # Если роль пользователя подрядчик, то он по умолчанию будет юр. лицом и его нельзя изменить

        person_input = self.browser.find_element_by_id('id_person')
        self.assertFalse(person_input.is_enabled())

        # person_input = Select(self.browser.find_element_by_id('id_person'))
        # person_input.select_by_value('entity')
        #
        # КОММЕНТАРИЙ К КОДУ ВЫШЕ
        # FIXME возможный баг. JS автоматически выбирает юр. лицо, однако аттрибут selected не применяется
        # к значению с юр. лицом. Тем не менее, в БД отправляется выбранное значение
        # либо на бэкенде стоит автоматическое присвоение, когда выбранно значение подрядчика.

        # заполняем дальше форму
        first_name_input = self.browser.find_element_by_id('id_first_name')
        first_name_input.send_keys('Тестовый')

        last_name_input = self.browser.find_element_by_id('id_last_name')
        last_name_input.send_keys('Пользователь')

        # Если пользователь юр. лицо, то ему доступен ввод названия предприятия
        entity_input = self.browser.find_element_by_id('id_entity_name')
        self.assertTrue(entity_input.is_enabled())

        # Продолжаем тестирование, теперь проверяем его в качестве Заявителя
        role_input = Select(self.browser.find_element_by_id('id_role'))
        role_input.select_by_value('custome')

        # Нам доступен выбор лица
        person_input = self.browser.find_element_by_id('id_person')
        self.assertTrue(person_input.is_enabled())

        # Но не доступен ввод документов
        permission = self.browser.find_element_by_id('id_permission')
        staff = self.browser.find_element_by_id('id_staff')
        equip = self.browser.find_element_by_id('id_equip')
        exp = self.browser.find_element_by_id('id_exp')
        reviews = self.browser.find_element_by_id('id_reviews')

        self.assertFalse(permission.is_enabled())
        self.assertFalse(staff.is_enabled())
        self.assertFalse(equip.is_enabled())
        self.assertFalse(exp.is_enabled())
        self.assertFalse(reviews.is_enabled())

        # В зависимости от лица можно вписывать его юридическое название

        entity_input = self.browser.find_element_by_id('id_entity_name')

        person_input = Select(self.browser.find_element_by_id('id_person'))

        person_input.select_by_value('entity')
        self.assertTrue(entity_input.is_enabled())

        person_input.select_by_value('entity')
        self.assertTrue(entity_input.is_enabled())
