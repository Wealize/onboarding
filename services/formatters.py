from services.constants import TICK_CHARACTER, SEPARATOR


class OnboardingFormatter:
    def __init__(self, config):
        self.config = config

    def get_onboarding_text(self, shell, apps):
        config = self.config
        return f'''
{config['title']}

{SEPARATOR}

{config['description']}

{config['description_apps']}

{SEPARATOR}

You are using {shell} shell

{apps}
'''

    def get_services_text(self, services):
        config = self.config

        return f'''
{SEPARATOR}

{config['description_services']}

{services}

{SEPARATOR}

{config['description_footer']}

'''
