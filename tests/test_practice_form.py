
from demoqa.models import app, data
from demoqa.models.data.user import student


def test_practice_form():
    app.registration_form.open_page() \
        .set_first_name('Тест') \
        .set_last_name('Тестов') \
        .set_email('test@test.test') \
        .set_gender('Female') \
        .set_user_number('8915999999') \
        .select_bday('08 Aug 1996') \
        .set_subjects('Accounting', 'Economics') \
        .set_hobbies('Sports', 'Music') \
        .set_photo('test.png') \
        .set_address('Россия, Москва') \
        .select_state('Haryana') \
        .select_city('Karnal') \
        .submit()

    app.registration_form.data_verification('Тест Тестов') \
        .data_verification('test@test.test') \
        .data_verification('Female') \
        .data_verification('8915999999') \
        .data_verification('08 August,1996') \
        .data_verification('Accounting, Economics') \
        .data_verification('Sports, Music') \
        .data_verification('test.png') \
        .data_verification('Россия, Москва') \
        .data_verification('Haryana Karnal')


def test_practice_form_step_object():
    app.registration.new_student()


def test_practice_form_fluent_page_objects():
    (
        app.registration_form.open_page()
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
                ('Subjects', data.user.get_string_values(student.subject)),
                ('Hobbies', data.user.get_string_values(student.hobbies)),
                ('Picture', student.photo),
                ('Address', student.address),
                ('State and City', f'{student.state} {student.city}')
            ]
        )
    )