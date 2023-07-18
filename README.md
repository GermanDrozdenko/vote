# Vote

## Requirements

* Python 3.10
* Django 4.2
* Pyenv-virtualenv

## Launch
Create virtual environment and install requirements
```
pyenv-virtualenv 3.10 vote-env
pyenv local vote-env
pip install -r requirements.txt
```

Apply migrations and create superuser
```
python manage.py migrate
python manage.py createsuperuser
```

Run server
```
python manage.py runserver
```

## API
(GET): All votings
```
api/votings
```

(GET): Voting by ID
```
api/voting/{ID}
```

(GET): Characters of a voting
```
api/voting/{ID}/characters
```

(GET): Winners of all votings
```
api/votings/winners
```

(GET): Winner of a voting by ID
```
api/voting/{ID}/winner
```

(POST): Add vote
```
api/voting/{ID}/add_vote
```
