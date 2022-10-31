import sys

from selene.support.shared import browser
from selenium.webdriver import Keys
from selene import Element


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select_date_of_bday(self, year, month, day):
        self.element.click()
        browser.element('.react-datepicker__year-select').element(f'[value={year}]').click()
        browser.element('.react-datepicker__month-select').element(f'[value={month}]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def select_date_of_bday_1(self, date):
        modifier_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        self.element.send_keys(modifier_key + 'a' + Keys.NULL).type(date).press_enter()
