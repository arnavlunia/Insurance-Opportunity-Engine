from faker import Faker
import random

fake = Faker()


def generate_client():
    age = random.randint(22, 60)

    return {
        "name": fake.name(),
        "age": age,
        "city": fake.city(),
        "salary": round(random.uniform(3, 50), 2) * 100000,  # INR
        "married": random.choice([True, False]),
        "children": random.randint(0, 3) if age > 28 else 0,
        "sip_amount": random.randint(2000, 50000),
        "nominee": fake.name()
    }