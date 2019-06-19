import subprocess

class OnboardingAppChecker:
    @classmethod
    def get_app_version(cls, app):
        output = cls.get_app_output(app)

        try:
            version = output.split('version')[1]
        except IndexError:
            version = output

        return version

    @classmethod
    def get_app_output(cls, app):
        output = subprocess.check_output(
            '{} --version'.format(app), shell=True)
        return output.decode('utf-8').strip()
