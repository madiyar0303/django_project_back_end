from django.test import TestCase
from django.template.defaultfilters import slugify
from main.models import Post


class ModelsTestCase(TestCase):
    def test_post_has_slug(self):
        post = Post.objects.create(title="My first post")

        post.author = "John Doe"
        post.save()
        self.assertEqual(post.slug, slugify(post.title))


def get_max(num1, num2):
    return num1 if num1 >= num2 else num2


class TestExample(TestCase):

    def test_get_max(self):
        self.assertEqual(get_max(4, 7), 7)
