import unittest

from services.formatters import OnboardingFormatter


class OnboardingRendererTestCase(unittest.TestCase):
    def setUp(self):
        self.shell = 'zsh'
        self.apps = 'ls instructions'
        self.services = 'ls instructions'
        self.config = {
            'title': 'My Company',
            'description': 'my description',
            'description_apps': 'my apps',
            'description_services': 'my apps',
            'description_footer': 'footer',
            'apps': {'ls': ''}
        }

    def test_get_onboarding_text(self):

        formatted_text = OnboardingFormatter(self.config).get_onboarding_text(
            self.shell, self.apps
        )

        self.assertIn(self.apps, formatted_text)
        self.assertIn(self.config['description'], formatted_text)

    def test_get_services_text(self):

        formatted_text = OnboardingFormatter(self.config).get_services_text(
            self.services
        )

        self.assertIn(self.services, formatted_text)
        self.assertIn(self.config['description_footer'], formatted_text)
