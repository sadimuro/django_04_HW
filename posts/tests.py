from django.test import TestCase, Client
from django.urls import reverse


class HelloTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    def test_hello(self):
        response = self.client.get(reverse("hello-view"))
        expected_data = "<h1>Hello</h1>"
        expected_header = "Alex"

        self.assertEqual(response.content.decode(), expected_data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.headers["name"], expected_header)


    def test_get_index(self):
        response_get = self.client.get(reverse("index-page"))
        response_post = self.client.post(reverse("index-page"))

        expected_get = "Главная страница"
        expected_post = "Не тот метод запроса"

        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(response_post.status_code, 200)
        self.assertEqual(response_get.content.decode(), expected_get)
        self.assertEqual(response_post.content.decode(), expected_post)
    def test_get_contacts(self):
        response_get = self.client.get(reverse("contacts"))

        expected_data = "Контакты"
        # yes fail because 'contacts' != 'Контакты'

        self.assertEqual(response_get.content.decode(), expected_data)
        self.assertEqual(response_get.status_code, 500)
    def test_get_about(self):
        response_get = self.client.get(reverse("about"))
        expected_data = "about"
        self.assertEqual(response_get.content.decode(), expected_data)
        self.assertEqual(response_get.status_code, 500)