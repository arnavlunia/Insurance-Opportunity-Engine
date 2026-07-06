from faker import Faker
import random

fake = Faker()

def generate_client():

    age = random.randint(22, 60)

    # -------------------------
    # REALISTIC DEMOGRAPHICS
    # -------------------------

    salary = random.lognormvariate(13, 0.7)  # heavy skew (MOST people low-mid income)

    married = random.random() < 0.35  # only 35% married

    children = 1 if (married and random.random() < 0.5 and age > 30) else 0

    sip_amount = random.choices(
        [0, 2000, 5000, 10000, 20000, 50000],
        weights=[35, 25, 20, 12, 6, 2]
    )[0]

    # -------------------------
    # NOMINEE (not always meaningful signal)
    # -------------------------

    nominee = fake.name() if random.random() < 0.7 else None

    return {
        "name": fake.name(),
        "age": age,
        "city": fake.city(),
        "salary": round(salary, 2),
        "married": married,
        "children": children,
        "sip_amount": sip_amount,
        "nominee": nominee
    }