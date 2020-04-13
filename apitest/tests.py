from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse

from apitest.views import test, home, login


class titlePageTest(TestCase):
    def test_loginpage_return_title_html(self):
        request = HttpResponse()
        response = login(request)
        self.assertIn(b"<title>AutotestPlat</title>", response.content)

