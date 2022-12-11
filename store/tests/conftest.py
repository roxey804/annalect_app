import pytest
import datetime
from blog.models import Post, Author, Tags

@pytest.fixture
def author_fixture():
    return Author.objects.create(
        name="Mock Author"
    )

@pytest.fixture
def tag_fixture():
    return Tags.objects.create(
        name="diy"
    )

@pytest.fixture
def blog_post_fixture():
    return Post.objects.create(
        slug='home-diy',
        title='Mock title',
        description='desc',
        date=datetime.date.today(),
        image='http://google.com',
        image_alt='alt text'
    )