from demoqa.models.pages.automation_practice_form import *

#browser.config.hold_browser_open = True


def test_practice_form():
    registration_form = RegistarationForm()
    registration_form.open_page('https://demoqa.com', '/automation-practice-form')
    registration_form.set_first_name('Тест')
    registration_form.set_last_name('Тестов')
    registration_form.set_email('test@test.test')
    registration_form.set_gender('Female')
    registration_form.set_user_number('8915999999')
    registration_form.select_bday('08 Aug 1996')
    registration_form.set_subject('Accounting', 'Economics')
    registration_form.set_hobbies('Sports', 'Music')
    registration_form.set_photo('../files_for_test/test.png')
    registration_form.set_address('Россия, Москва')
    registration_form.select_state('Haryana')
    registration_form.select_city('Karnal')
    registration_form.submit()

    registration_form.data_verification('Тест Тестов')
    registration_form.data_verification('test@test.test')
    registration_form.data_verification('Female')
    registration_form.data_verification('8915999999')
    registration_form.data_verification('08 August,1996')
    registration_form.data_verification('Accounting, Economics')
    registration_form.data_verification('Sports, Music')
    registration_form.data_verification('test.png')
    registration_form.data_verification('Россия, Москва')
    registration_form.data_verification('Haryana Karnal')