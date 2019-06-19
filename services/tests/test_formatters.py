import os
import unittest

from services.renderer import OnboardingRenderer


class OnboardingRendererTestCase(unittest.TestCase):
    def setUp(self):
        self.config = {}
