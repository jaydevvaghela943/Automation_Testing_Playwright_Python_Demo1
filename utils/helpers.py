import random
import string


def generate_random_email():

    random_string = ''.join(
        random.choices(
            string.ascii_lowercase,
            k=5
        )
    )

    return f"{random_string}@test.com"