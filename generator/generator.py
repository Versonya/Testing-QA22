import random

from data.data import Person
from faker import Faker
from data.data import Table

faker_ru = Faker('ru_Ru')
Faker.seed()



def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )

def generate_row():
    yield Table(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(10, 100),
        salary=random.randint(1000, 100000),
        department=faker_ru.job(),
    )