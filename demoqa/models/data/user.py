from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Gender(Enum):
    Male = '1'
    Female = 'Female'
    Other = '3'


class Hobby(Enum):
    Music = 'Music'
    Reading = 'Reading'
    Sports = 'Sports'


class Subject(Enum):
    Maths = 'Maths'
    Accounting = 'Accounting'
    Arts = 'Arts'
    Social_Studies = 'Social Studies'
    English = 'English'
    Chemistry = 'Chemistry'
    Physics = 'Physics'
    Computer_Science = 'Computer Science'
    Economics = 'Economics'
    History = 'History'
    Civics = 'Civics'
    Hindi = 'Hindi'
    Biology = 'Biology'
    Commerce = 'Commerce'


def get_string_values(subjects: Tuple):
    ret: str = ''
    for subject in subjects:
        ret = ret + str(subject.name) + ', '
    ret = ret.rstrip(', ')
    return ret


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Tuple[Gender]
    number: str
    bday: str
    subject: Tuple[Subject]
    hobbies: Tuple[Hobby]
    photo: str
    address: str
    state: str
    city: str


student = User(first_name='Тест', last_name='Тестов', email='test@test.test',
               gender=Gender.Female.name, number='8915999999', bday='08 Aug 1996',
               subject=(Subject.Accounting, Subject.Economics), hobbies=(Hobby.Sports, Hobby.Music),
               photo='test.png', address='Россия, Москва', state='Haryana', city='Karnal')
