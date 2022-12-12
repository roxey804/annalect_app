import pytest
from store.models import Product
from django.contrib.auth.models import User

@pytest.fixture
def product_fixture():
    return Product.objects.create(
        name="Mock product",
        description="desc",
        price=1,
    )

@pytest.fixture
def normal_user_fixture():
    return User.objects.create_user(
        username="test_normal_user", 
        password="test",
        is_superuser=False,
        is_staff=False,
    )
