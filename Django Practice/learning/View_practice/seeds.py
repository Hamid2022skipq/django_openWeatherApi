# https://faker.readthedocs.io/en/master/fakerclass.html#upgrade-guide
from faker import Faker
fake = Faker()
from .models import *
import random
def seed_db(n=10)->None:
    try:
        for i in range(0,n):
            name=fake.name()
            # title=fake.title()
            # des=fake.description()
            email=fake.email()
            age=random.randint(18,30)
            fee=random.randint(2000,50000)
        
            service_obj=service.objects.create(
                name=name,
                # title=title,
                # des=des,
                email=email,
                age=age,
                fee=fee,
            )
    except Exception as e:
        print(e)    