import pytest
from store.views import admin_page

@pytest.mark.django_db #this property allows pytest access to the django db
def test_create_product(product_fixture):
    test_product = product_fixture
    assert test_product.name == 'Mock product'

@pytest.mark.django_db # not sure if need to test str methods unless complex?
def test_str_method(product_fixture):
    post_1 = product_fixture
    assert post_1.__str__() == 'Mock product'

def test_django_admin(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200

def test_admin_view(rf, admin_user):
    request = rf.get('/admin_page')
    request.user = admin_user
    response = admin_page(request)
    assert response.status_code == 200
    assert b'Since you are an admin, you can view this page' in response.content 

@pytest.mark.django_db
def test_normal_user(rf, normal_user_fixture):
    request = rf.get('/admin_page')
    request.user = normal_user_fixture
    response = admin_page(request)
    assert response.status_code == 200
    assert b'Sorry, this content is available to admin only' in response.content
