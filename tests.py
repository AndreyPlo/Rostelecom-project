import pytest
from pages.auth_page import AuthPage
from pages.config_page import RegPage


# TC-001
def test_start_page_is_correct(web_browser):
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert phone_tab_class == "rt-tab rt-tab--small rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()
    assert page.auth_title.get_text() == "Авторизация"
    assert page.logo_lk.get_text() == "Личный кабинет"


# TC-002
@pytest.mark.xfail(reason="Расположение левого и правого блоков не соответсвует ТЗ")
def test_location_of_page_blocks(web_browser):
    page = AuthPage(web_browser)
    assert page.auth_form.find(timeout=1)
    assert page.lk_form.find(timeout=1)


# TC-003
@pytest.mark.xfail(reason="Таб 'Телефон'")
def test_phone_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Телефон"


# TC-004
@pytest.mark.xfail(reason="Таб 'Почта'")
def test_email_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.email_tab.get_text() == "Почта"


# TC-005
@pytest.mark.xfail(reason="Таб 'Логин'")
def test_login_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.login_tab.get_text() == "Логин"


# TC-006
@pytest.mark.xfail(reason="Таб 'Лицевой счет'")
def test_personal_account_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.personal_account_tab.get_text() == "Лицевой счет"


# ТС-007
@pytest.mark.xfail(reason="Кнопка должна иметь текст 'Продолжить'")
def test_registration_page_and_continue_button(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.name_field_text.get_text() == "Имя"
    assert reg_page.last_name_field_text.get_text() == "Фамилия"
    assert reg_page.region_field_text.get_text() == "Регион"
    assert reg_page.email_or_mobile_phone_field_text.get_text() == "E-mail или мобильный телефон"
    assert reg_page.password_field_text.get_text() == "Пароль"
    assert reg_page.password_confirmation_field_text.get_text() == "Подтверждение пароля"
    assert reg_page.continue_button.get_text() == "Продолжить"


# ТС-008
def test_registration_page_with_empty_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('')
    reg_page.last_name_field.send_keys("Иваноф")
    reg_page.email_or_mobile_phone_field.send_keys("ivanof@gmail.com")
    reg_page.password_field.send_keys("Ivanof123456!")
    reg_page.password_confirmation_field.send_keys("Ivanof123456!")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Заполнить поле кириллицей от 2 до 30 символов"


# ТС-009
def test_registration_page_with_empty_lastname_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Иван')
    reg_page.last_name_field.send_keys("")
    reg_page.email_or_mobile_phone_field.send_keys("ivanof@gmail.com")
    reg_page.password_field.send_keys("Ivanof123456!")
    reg_page.password_confirmation_field.send_keys("Ivanof123456!")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Заполнить поле кириллицей от 2 до 30 символов"


# ТС-010
def test_registration_page_with_empty_email_or_mobile_phone_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Иван')
    reg_page.last_name_field.send_keys("Иваноф")
    reg_page.email_or_mobile_phone_field.send_keys("")
    reg_page.password_field.send_keys("Ivanof123456!")
    reg_page.password_confirmation_field.send_keys("Ivanof123456!")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Заполнить поле от 2 до 30 символов"


# ТС-011
def test_registration_page_with_empty_password_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Иван')
    reg_page.last_name_field.send_keys("Иваноф")
    reg_page.email_or_mobile_phone_field.send_keys("ivanof@gmail.com")
    reg_page.password_field.send_keys("")
    reg_page.password_confirmation_field.send_keys("")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Заполнить поле кириллицей от 2 до 30 символов"


# ТС-012
def test_registration_with_an_incorrect_value_in_the_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('И')
    reg_page.last_name_field.send_keys("Иваноф")
    reg_page.email_or_mobile_phone_field.send_keys("ivanof@gmail.com")
    reg_page.password_field.send_keys("Ivanof123456!")
    reg_page.password_confirmation_field.send_keys("Ivanof123456!")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Заполнить поле кириллицей от 2 до 30 символов"


# ТС-013
def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("Иванофффффффффффффффффффффффффф")
    reg_page.email_or_mobile_phone_field.send_keys("ivanof@gmail.com")
    reg_page.password_field.send_keys("Ivanof123456!")
    reg_page.password_confirmation_field.send_keys("Ivanof123456!")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Заполнить поле кириллицей от 2 до 30 символов"


# ТС-014
def test_registration_of_an_already_registered_user(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("Иваноф")
    reg_page.email_or_mobile_phone_field.send_keys("+79216367530")
    reg_page.password_field.send_keys("Ivanof123456!")
    reg_page.password_confirmation_field.send_keys("Ivanof123456!")
    reg_page.continue_button.click()
    assert reg_page.notification_form.is_visible


# ТС-015
def test_incorrect_password_during_registration(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("Иваноф")
    reg_page.email_or_mobile_phone_field.send_keys("ivanof@gmail.com")
    reg_page.password_field.send_keys("Ivanof")
    reg_page.password_confirmation_field.send_keys("Ivanof")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Длина пароля должна быть не менее 8 символов"


# ТС-016
def test_instead_of_cyrillic_invalid_characters(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("!!!!!!!!!!!!")
    reg_page.email_or_mobile_phone_field.send_keys("ivanof@gmail.com")
    reg_page.password_field.send_keys("Ivanof123456!")
    reg_page.password_confirmation_field.send_keys("Ivanof123456!")
    reg_page.continue_button.click()
    assert reg_page.message_must_be_filled_in_cyrillic.get_text() == "Заполнить поле кириллицей от 2 до 30 символов"


# ТС-017
def test_password_and_password_confirmation_do_not_match(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("Иваноф")
    reg_page.email_or_mobile_phone_field.send_keys("ivanof@gmail.com")
    reg_page.password_field.send_keys("Ivanof123456!")
    reg_page.password_confirmation_field.send_keys("Ivanof")
    reg_page.continue_button.click()
    assert reg_page.message_passwords_dont_match.get_text() == "Пароли не совпадают"


# ТС-018
def test_authorization_of_a_user_with_an_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys("+79216367530")
    page.password.send_keys("Ivanof")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или пароль"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')

# ТС-019
def test_invalid_email_or_mobile_phone(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("Иваноф")
    reg_page.email_or_mobile_phone_field.send_keys("12345")
    reg_page.password_field.send_keys("Ivanof123456!")
    reg_page.password_confirmation_field.send_keys("Ivanof123456!")
    reg_page.continue_button.click()
    assert reg_page.message_enter_the_phone_in_the_format.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ" \
                                                                        "email в формате example@gmail.com"



# ТС-020
def test_authorisation_valid(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys("+79216367530")
    page.password.send_keys("Ivanof123456!")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()