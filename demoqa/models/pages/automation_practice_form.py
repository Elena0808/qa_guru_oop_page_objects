from typing import Tuple

from selene import have, command
from selene.support.shared import browser

from demoqa.models import data
from demoqa.models.controls.checkbox import select_checkbox
from demoqa.models.controls.dropdown import DropDown
from demoqa.models.controls.datepicker import DatePicker
from demoqa.models.controls.radiobutton import select_radiobutton
from demoqa.models.data.user import User, student, Subject, Hobby
from demoqa.utils.path import abs_path


class RegistarationForm:
    def __init__(self):
        self.bday = DatePicker(browser.element('#dateOfBirthInput'))

    def open_page(self, url='https://demoqa.com/automation-practice-form'):
        browser.config.window_height, browser.config.window_width = 1000, 1000
        browser.open(url)
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

    def set_gender(self, option: str):
        select_radiobutton('[for^=gender-radio]', option).first.click()
        return self

    def set_user_number(self, user_number):
        browser.element('#userNumber').type(user_number)
        return self

    def select_bday(self, data):
        self.bday.select_date_of_bday_1(data)
        return self

    def set_subjects(self, subject_1, subject_2):
        browser.element('[id="subjectsInput"]').type(subject_1).press_enter() \
            .type(subject_2).press_enter()
        return self

    def set_subject(self, subjects: Tuple[Subject]):
        for subject in subjects:
            browser.element('[id="subjectsInput"]').type(subject.name).press_enter()
        return self

    def set_hobbies(self, option: str, option1: str):
        select_checkbox('[for^=hobbies-checkbox]', option).first.click()
        select_checkbox('[for^=hobbies-checkbox]', option1).first.click().perform(command.js.scroll_into_view)
        return self

    def set_hobby(self, hobbies: Tuple[Hobby]):
        for hobby in hobbies:
            select_checkbox('[for^=hobbies-checkbox]', hobby.name).first.click().perform(command.js.scroll_into_view)
        return self

    def set_photo(self, photo):
        p = abs_path(photo)
        print(p)
        browser.element('[id="uploadPicture"]').send_keys(p)
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

    def data_verification(self, parameter_name: str):
        browser.element('.table-responsive').should(have.text(parameter_name))
        return self

    def check_values(self, values):
        for key, value in values:
            browser.element('.table-responsive').should(have.text(key))
            browser.element('.table-responsive').should(have.text(value))
        return self


class RegistrationStudent:
    def __init__(self):
        self.registration = RegistarationForm()

    def new_student(self):
        (
            self.registration.open_page('https://demoqa.com/automation-practice-form')
                .set_first_name(student.first_name)
                .set_last_name(student.last_name)
                .set_email(student.email)
                .set_gender(student.gender)
                .set_user_number(student.number)
                .select_bday(student.bday)
                .set_subject(student.subject)
                .set_hobby(student.hobbies)
                .set_photo(student.photo)
                .set_address(student.address)
                .select_state(student.state)
                .select_city(student.city)
                .submit()
                .check_values(
                [
                    ('Student Name', f'{student.first_name} {student.last_name}'),
                    ('Student Email', student.email),
                    ('Gender', student.gender),
                    ('Mobile', student.number),
                    ('Date of Birth', '08 August,1996'),
                    ('Subjects', data.user.get_string_values(student.subject)),
                    ('Hobbies', data.user.get_string_values(student.hobbies)),
                    ('Picture', student.photo),
                    ('Address', student.address),
                    ('State and City', f'{student.state} {student.city}')
                ]
            )
        )