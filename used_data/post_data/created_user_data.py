from faker import Faker
from mimesis import Person

person = Person('ru')

fake = Faker('ru_RU')

phone = person.telephone(mask="+7 9## ###-##-##")

pyload = {
    "last_name": fake.last_name(),
    "first_name": fake.first_name(),
    "patronymic": fake.last_name(),
    "phone": phone,
    "username": phone,
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
