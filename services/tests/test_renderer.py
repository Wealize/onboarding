import os
import unittest
from unittest import mock
import subprocess

from services.renderer import OnboardingRenderer
from services.checker import OnboardingAppChecker


class OnboardingRendererTestCase(unittest.TestCase):
    def test_render_apps_returns_empty(self):
        config = {'apps': {}}

        apps = OnboardingRenderer(config).render_apps()

        self.assertEqual(apps, [])

    @mock.patch.object(OnboardingAppChecker, 'get_app_version')
    def test_render_apps_returns_failed_apps(self, get_app_version):
        get_app_version.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd='ls')
        config = {
            'apps': {'ls': ''}
        }

        apps = OnboardingRenderer(config).render_apps()

        self.assertEqual(apps, ['\x1b[31m✘ ls \n\x1b[0m'])

    @mock.patch.object(OnboardingAppChecker, 'get_app_version')
    def test_render_apps_returns_valid_apps(self, get_app_version):
        get_app_version.return_value = ' 1.2.0'
        config = {
            'apps': {'ls': ''}
        }

        apps = OnboardingRenderer(config).render_apps()

        self.assertEqual(apps, ['\x1b[32m✓ ls  1.2.0\x1b[0m'])

    def test_render_services_returns_empty(self):
        config = {'services': {}}

        services = OnboardingRenderer(config).render_services()

        self.assertEqual(services, [])

    def test_render_services_returns_valid_services(self):
        my_service = {'myService': 'instructions'}
        expected_styled_service = '\x1b[34mMyservice\n\x1b[0minstructions'
        config = {
            'services': my_service
        }

        services = OnboardingRenderer(config).render_services()

        self.assertEqual(services, [expected_styled_service])
