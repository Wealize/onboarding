import os
import subprocess

import yaml
import click

from services.formatters import OnboardingFormatter
from services.renderer import OnboardingRenderer


@click.command()
def onboarding():
    config_path = os.environ.get('ONBOARDING_FILE_PATH', 'config.yml')
    config = yaml.load(open(config_path, 'r'), Loader=yaml.FullLoader)

    formatter = OnboardingFormatter(config)
    renderer = OnboardingRenderer(config)

    shell = subprocess.check_output('echo $SHELL', shell=True)
    shell = shell.decode('utf-8').strip()

    apps = '\n'.join(renderer.render_apps())
    services = '\n'.join(renderer.render_services())

    click.echo(formatter.get_onboarding_text(shell, apps))
    want_continue = click.confirm(
        'Do you want to see the services you need access to?')

    if want_continue:
        click.echo(formatter.get_services_text(services))


if __name__ == '__main__':
    onboarding()
