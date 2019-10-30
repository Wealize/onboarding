import subprocess

import click

from services.constants import TICK_CHARACTER, ERROR_CHARACTER
from services.checker import OnboardingAppChecker


class OnboardingRenderer:
    app_checker = OnboardingAppChecker

    def __init__(self, config):
        self.config = config

    def render_apps(self):
        apps = []

        for app, instructions in self.config['apps'].items():
            try:
                version = self.app_checker.get_app_version(app)

                apps.append(click.style(
                    f'{TICK_CHARACTER} {app} {version}', fg='green'))
            except subprocess.CalledProcessError:
                apps.append(click.style(
                    f'{ERROR_CHARACTER} {app} \n{instructions}', fg='red'))

        return apps

    def render_services(self):
        services = []

        for service, instructions in self.config['services'].items():
            services.append(
                ''.join([click.style(f'{service.capitalize()}\n', fg='blue'),
                         f'{instructions}']
                        ))

        return services
