import os
import unittest
from unittest import mock
import subprocess

from services.checker import OnboardingAppChecker


class OnboardingAppCheckerTestCase(unittest.TestCase):

    @mock.patch.object(OnboardingAppChecker, 'get_app_output')
    def test_get_app_version_with_valid_version(self, get_app_output):
        expected_value = 'output'
        get_app_output.return_value = expected_value

        version = OnboardingAppChecker.get_app_version('ls')

        self.assertEqual(version, expected_value)

    @mock.patch.object(OnboardingAppChecker, 'get_app_output')
    def test_get_app_version_with_no_version(self, get_app_output):
        get_app_output.return_value = f'version 1.2.0'

        version = OnboardingAppChecker.get_app_version('ls')

        self.assertEqual(version, ' 1.2.0')

    @mock.patch.object(subprocess, 'check_output')
    def test_get_app_output(self, check_output):
        expected_output = 'version 1.2.0'
        check_output.return_value = b'version 1.2.0'

        output = OnboardingAppChecker.get_app_output('ls')

        self.assertEqual(output, expected_output)
