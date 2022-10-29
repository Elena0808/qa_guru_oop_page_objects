from selene.support.shared import browser
from selenium.webdriver import Keys


def select_date_of_bday():
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').element('[value="1996"]').click()
    browser.element('.react-datepicker__month-select').element('[value="7"]').click()
    browser.element('.react-datepicker__day--008').click()
    return select_date_of_bday()


def select_date_of_bday_1(date):
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type(date).press_enter()
   # browser.element('#dateOfBirthInput').send_keys(Keys.COMMAND, 'a').type(date).press_enter()