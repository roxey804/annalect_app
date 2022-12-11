import pytest
from store.models import Product

@pytest.fixture
def product_fixture():
    return Product.objects.create(
        name="Mock product",
        description="desc",
        price=1,
    )
