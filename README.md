# Team Onboarding app 🤓

![Screenshot 2019-06-18 at 19 34 10](https://user-images.githubusercontent.com/488556/59706185-3a765680-9200-11e9-90ce-490c377e7016.png)

![Screenshot 2019-06-18 at 19 34 24](https://user-images.githubusercontent.com/488556/59706184-3a765680-9200-11e9-9a29-a10e7fe8fff1.png)

## Installation

You need to install pipenv

```bash
pip3 install pipenv
pipenv --python 3.7
pipenv install
```

Then you can create a config file for your team (YAML) and set it with the `ONBOARDING_FILE_PATH` envvar.

By default it loads our config file 😁, [You can use it as example](https://github.com/TheNeonProject/onboarding/blob/master/config.yml).

## Running from terminal

```bash
pipenv run python cli.py
```

## Running from VS Code

You can open the VS Code, go to the Debug Tab and click the play button to run the script ✨.
