import pytest
from django.urls import reverse
from store.models import Product

@pytest.mark.django_db #this allows pytest access to the django db
def test_create_product(product_fixture):
    test_product = product_fixture
    assert test_product.name == 'Mock product'


@pytest.mark.django_db # not sure if need to test str methods unless complex?
def test_str_method(product_fixture):
    post_1 = product_fixture
    assert post_1.__str__() == 'Mock product'


@pytest.mark.django_db
def test_posts(client):
    response = client.get('http://localhost:8000/')
    assert response.status_code == 200