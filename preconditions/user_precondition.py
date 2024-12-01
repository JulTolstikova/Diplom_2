from data import generate_random_string


def data_user():
    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": f"{email}@mail.ru",
        "password": f"{password}",
        "name": f"{name}"
    }
    return payload


def data_authorization_user(data_user):
    payload = {
        "email": data_user["email"],
        "password": data_user["password"],
    }
    return payload
