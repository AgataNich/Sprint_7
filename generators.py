from faker import Faker
import random, string

fake = Faker()


def login_generator():
    generator_login = fake.user_name()
    return generator_login


def password_generator():
    generator_password = fake.random_number(5)
    return generator_password


def name_generator():
    generate_name = fake.first_name()
    return generate_name


def login_generator():
    base = 'user'
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f'{base}_{suffix}'

