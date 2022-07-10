# Monkey Island REST API

Monkey Island REST API for development, testing and learning purposes.

## Installation

### Requirements

Before continue, you will need at least `Pipenv` and Python 3.7 and basic knowledge of the terminal.

### Running development environment

```shell
python -m pipenv --python 3.7
python -m pipenv install
python -m pipenv run python MonkeyIslandAPI/manage.py migrate
python -m pipenv run python MonkeyIslandAPI/manage.py loaddata --app app src/initial.json
python -m pipenv run python MonkeyIslandAPI/manage.py runserver
```

### Docker

Make sure you have Docker previously installed on your system.

```shell
docker-compose run web python src/manage.py migrate
docker-compose run web python src/manage.py loaddata --app app src/initial.json
docker-compose up
```

## Docs

| Endpoint            | Params                   | Description                                            |
|:--------------------|:-------------------------|:-------------------------------------------------------|
|`api/v1/characters`  |`?role=<MC/SC>` (optional)| Returns a list of available characters on Mêlée Island.|
|`api/v1/pirates   `  |`?role=<MC/SC>` (optional)| Returns a list of available buccaneers on Mêlée Island.|
|`api/v1/insults   `  |`?role=<MC/SC>` (optional)| Returns a list of available buccaneers on Mêlée Island.|
