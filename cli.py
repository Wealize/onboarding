import subprocess

import click

TICK_CHARACTER = u'\u2713'
ERROR_CHARACTER = u'\u2718'


@click.command()
def onboarding():
    """Simple aplication controlling you have al the tools needed for TNP"""
    apps = ['fzf', 'git', 'code', 'docker', 'docker-compose', 'pepe']
    shell = subprocess.check_output('echo $SHELL', shell=True)

    click.echo('You are using {} shell'.format(shell))

    for app in apps:
        try:
            subprocess.check_output(
                'which {}'.format(app), shell=True)
            click.secho('{} {}'.format(TICK_CHARACTER, app), fg='green')
        except subprocess.CalledProcessError as e:
            pass
            click.secho('{} {}'.format(ERROR_CHARACTER, app), fg='red')


if __name__ == '__main__':
    onboarding()
