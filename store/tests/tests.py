import pytest
from django.urls import reverse
from blog.models import Post, Author, Tags
import datetime


@pytest.mark.django_db #this allows pytest access to the django db
def test_create_author():
    test_author = Author.objects.create(name='test author')
    assert test_author.name == 'test author'

@pytest.mark.django_db 
def test_create_tag():
    test_tag = Tags.objects.create(name='test tag')
    assert test_tag.name == 'test tag'

@pytest.mark.django_db
def test_blog_post_creation(blog_post_fixture, author_fixture, tag_fixture):
    test_blog = blog_post_fixture
    test_blog.author.set([author_fixture])
    test_blog.tags.set([tag_fixture])
    assert test_blog.title == 'Mock title'
    assert test_blog.slug == 'home-diy'
    assert test_blog.tags.select_related().first().name == 'diy' # how to simplify m2m tests?
    assert test_blog.author.select_related().first().name == 'Mock Author'

@pytest.mark.django_db
def test_can_create_posts_same_title_date(blog_post_fixture):
    test_blog_1 = blog_post_fixture
    test_blog_2 = Post.objects.create(
        slug='christmas',
        title='mock title',
        date=datetime.date.today(),
        image_alt='alt text'
    )
    assert test_blog_1
    assert test_blog_2

@pytest.mark.django_db
def test_cannot_create_posts_same_slug(blog_post_fixture):
    test_blog_1 = blog_post_fixture
    from django.db import IntegrityError
    with pytest.raises(IntegrityError) as e:
        test_blog_2 = Post.objects.create(
            slug='home-diy',
            title='Mock title',
            description='desc',
            date=datetime.date.today(),
            image='http://google.com',
            image_alt='alt text'
        )

@pytest.mark.django_db # not sure if need to test str methods unless complex?
def test_str_method(blog_post_fixture):
    post_1 = blog_post_fixture
    assert post_1.__str__() == 'Mock title'


@pytest.mark.django_db
def test_posts(client):
    response = client.get('http://localhost:8000/api/posts')
    assert response.status_code == 200