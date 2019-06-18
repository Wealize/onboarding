import subprocess

import click

from constants import TICK_CHARACTER, ERROR_CHARACTER


def render_apps(config):
    apps = []

    for app, instructions in config['apps'].items():
        try:
            output = subprocess.check_output(
                '{} --version'.format(app), shell=True)
            output = output.decode('utf-8').strip()

            try:
                version = output.split('version')[1]
            except IndexError:
                version = output

            apps.append(click.style(
                f'{TICK_CHARACTER} {app} {version}', fg='green'))
        except subprocess.CalledProcessError as e:
            apps.append(click.style(f'{ERROR_CHARACTER} {app} \n{instructions}', fg='red'))

    return apps


def render_services(config):
    services = []

    for service, instructions in config['services'].items():
        services.append(
            ''.join([click.style(f'{service.capitalize()}\n', fg='blue'),
                     f'{instructions}']
        ))

    return services
