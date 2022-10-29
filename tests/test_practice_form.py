from demoqa.models.controls import datepicker
from demoqa.models.pages.automation_practice_form import *
#browser.config.hold_browser_open = True


def test_practice_form():
    open_page('https://demoqa.com', '/automation-practice-form')
    set_first_name('Тест')
    set_last_name('Тестов')
    set_email('test@test.test')
    set_gender('Female')
    set_user_number('8915999999')
    datepicker.select_date_of_bday_1('08 Aug 1996')
    set_subject('Accounting', 'Economics')
    set_hobbies('Sports', 'Music')
    set_photo('../files_for_test/test.png')
    set_address('Россия, Москва')
    select_state('Haryana')
    select_city('Karnal')
    submit()

    data_verification('Тест Тестов')
    data_verification('test@test.test')
    data_verification('Female')
    data_verification('8915999999')
    data_verification('08 August,1996')
    data_verification('Accounting, Economics')
    data_verification('Sports, Music')
    data_verification('test.png')
    data_verification('Россия, Москва')
    data_verification('Haryana Karnal')