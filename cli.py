import re
import os
import json
import subprocess

import yaml
import click

from constants import TICK_CHARACTER, ERROR_CHARACTER, SEPARATOR
from services import render_apps, render_services


@click.command()
def onboarding():
    config_path = os.environ.get('ONBOARDING_FILE_PATH', 'config.yml')
    config = yaml.load(open(config_path, 'r'), Loader=yaml.FullLoader)

    shell = subprocess.check_output('echo $SHELL', shell=True)
    shell = shell.decode('utf-8').strip()

    apps = '\n'.join(render_apps(config))
    services = '\n'.join(render_services(config))

    click.echo(f'''
{config['title']}

{SEPARATOR}

{config['description']}

{config['description_apps']}

{SEPARATOR}

You are using {shell} shell

{apps}
''')

    want_continue = click.confirm(
        'Do you want to see the services you need access to?')

    click.secho(
        f'''
{SEPARATOR}

{config['description_services']}

{services}

{SEPARATOR}

{config['description_footer']}

''')


if __name__ == '__main__':
    onboarding()
