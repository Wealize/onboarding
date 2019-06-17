import subprocess

import click

TICK_CHARACTER = u'\u2713'
ERROR_CHARACTER = u'\u2718'
TITLE = ''
DESCRIPTION = ''
APPS = ['fzf', 'git', 'code', 'docker', 'docker-compose']
SERVICES = ['abstract', 'slack', 'github', 'gitlab', 'codacy', 'factorial']


@click.command()
def onboarding():
    """Simple aplication controlling you have al the tools needed for TNP"""
    shell = subprocess.check_output('echo $SHELL', shell=True)
    shell = shell.decode('utf-8').strip()

    click.echo('-------------------------------------')
    click.echo('You are using {} shell'.format(shell))

    for app in APPS:
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


if __name__ == '__main__':
    onboarding()
