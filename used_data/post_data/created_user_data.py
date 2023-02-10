from faker import Faker
fake = Faker('ru_RU')

pyload = {
    "last_name": fake.last_name(),
    "first_name": fake.first_name(),
    "patronymic": fake.last_name(),
    "phone": "+7 (969) 696-69-69",
    "username": "+7 (969) 696-69-69",
    "email": fake.email(),
    "extra": {
        "with_services": True,
        "with_devices": True
    },
    "residency": {
        "type": "apartment",
        "id": "63a60076f93dfe52cfd86cd1"
    },
    "category": "client"
}
