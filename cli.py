import os
import json
import subprocess

import yaml
import click

TICK_CHARACTER = u'\u2713'
ERROR_CHARACTER = u'\u2718'


@click.command()
def onboarding():
    """Simple aplication controlling you have al the tools needed for TNP"""
    config_path = os.environ.get('ONBOARDING_FILE_PATH', 'config.yml')
    config = yaml.load(open(config_path, 'r'))

    shell = subprocess.check_output('echo $SHELL', shell=True)
    shell = shell.decode('utf-8').strip()

    click.secho(config['title'])
    click.secho(config['description'])
    click.secho(config['description_apps'])

    click.echo('-------------------------------------')
    click.echo('You are using {} shell'.format(shell))

    for app, instructions in config['apps'].items():
        try:
            output = subprocess.check_output(
                '{} --version'.format(app), shell=True)
            output = output.decode('utf-8').strip()

            try:
                version = output.split('version')[1]
            except IndexError:
                version = output

            click.secho('{} {}: {}'.format(
                TICK_CHARACTER, app, version), fg='green')
        except subprocess.CalledProcessError as e:
            click.secho('{} {}'.format(ERROR_CHARACTER, app), fg='red')
            click.secho(instructions, fg='white')

    want_continue = click.confirm('Do you want to see the services you need access to?')

    if want_continue:
        click.secho(config['description_services'])
        [click.secho('{}\n\n{}\n'.format(service.capitalize(), instructions), fg='blue')
        for service, instructions in config['services'].items()]

    click.secho(config['description_footer'])


if __name__ == '__main__':
    onboarding()
