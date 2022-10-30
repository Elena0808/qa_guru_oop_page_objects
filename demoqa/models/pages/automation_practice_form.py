from selene import have, command
from selene.support.shared import browser
from demoqa.models.controls.checkbox import select_checkbox
from demoqa.models.controls.dropdown import DropDown
from demoqa.models.controls.datepicker import DatePicker
from demoqa.models.controls.radiobutton import select_radiobutton
from demoqa.utils.path import abs_path


class RegistarationForm:
    def __init__(self):
        self.bday = DatePicker(browser.element('#dateOfBirthInput'))

    def open_page(self, url, resourses):
        browser.config.window_height, browser.config.window_width = 1000, 1000
        browser.open(url + resourses)
        return self

    def set_first_name(self, first_name):
        browser.element('#firstName').type(first_name)
        return self

    def set_last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    def set_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def set_gender(self, option):
        select_radiobutton('[for^=gender-radio]', option).first.click()
        return self

    def set_user_number(self, user_number):
        browser.element('#userNumber').type(user_number)
        return self

    def select_bday(self, data):
        self.bday.select_date_of_bday_1(data)
        return self

    def set_subject(self, subject_1, subject_2):
        browser.element('[id="subjectsInput"]').type(subject_1).press_enter() \
            .type(subject_2).press_enter()
        return self

    def set_hobbies(self, option, option1):
        select_checkbox('[for^=hobbies-checkbox]', option).first.click()
        select_checkbox('[for^=hobbies-checkbox]', option1).first.click().perform(command.js.scroll_into_view)
        return self

    def set_photo(self, photo):
        browser.element('[id="uploadPicture"]').send_keys(abs_path(photo))
        return self

    def set_address(self, current_address):
        browser.element('[id="currentAddress"]').type(current_address)
        return self

    def select_state(self, state):
        state_dropdown = DropDown(browser.element('#state'))
        state_dropdown.select(state)
        return self

    def select_city(self, city):
        city_dropdown = DropDown(browser.element('#city'))
        city_dropdown.select(city)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def data_verification(self, parameter_name):
        browser.element('.table-responsive').should(have.text(parameter_name))
        return self
