from django.test import TestCase
from django.urls import reverse, resolve

from website.views import WelcomeToWebsite


class WebsiteUrlsTest(TestCase):

    def test_welcome_view_urls(self):
        url = reverse('website:welcome')
        self.assertEqual(resolve(url).func.view_class, WelcomeToWebsite)
