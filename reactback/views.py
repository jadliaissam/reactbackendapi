import pytz
from django.http import JsonResponse
from django.shortcuts import render
from reactbackapp.models import MyUser, Product, Operation
import random
from faker import Faker


def home(request):
    return render(request, 'index.html')


def init_data(request):
    fake = Faker()
    Operation.objects.all().delete()
    Product.objects.all().delete()
    users = MyUser.objects.all()
    for user in users[1:]:
        user.delete()

    MyUser.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), username=fake.word(), password="pass", avatar="upload/users/default1.png")
    MyUser.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), username=fake.word(), password="pass", avatar="upload/users/default2.png")
    MyUser.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), username=fake.word(), password="pass", avatar="upload/users/default3.png")
    pds = []
    for i in range(20):
        pds.append(Product(title=fake.name(), description=fake.text(), image="upload/products/product{}.png".format(random.choice(range(1, 15)))))
    Product.objects.bulk_create(pds)

    ids_users = [x['id'] for x in MyUser.objects.values('id')]
    ids_products = [x['id'] for x in Product.objects.values('id')]
    ids_types = [1, 2]
    quantities = [12, 10, 6, 2, 5, 1, 44, 10, 3, 20, 17, 9, 20, 27, 10]
    ops = []
    for i in range(500):
        ops.append(
            Operation(
                type=random.choice(ids_types),
                operation_product_id=random.choice(ids_products),
                operation_user_id=random.choice(ids_users),
                quantity=random.choice(quantities),
                description=fake.text(),
                created_at=fake.date_between(start_date='-5y', end_date='today')
            ))
    Operation.objects.bulk_create(ops)
    return JsonResponse({'msg': 'Import Ok'})