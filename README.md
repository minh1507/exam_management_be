## Quick start

* Required: Python@3.12
* Project use pipenv to manage library

```bash
  pip install pipenv
```

* Clone project from github. 
```bash
  git clone <repo-name>
  cd <repo-name>
  pipenv install
```

* If version pipfile is missmatch then do this command 
```bash
  pipenv lock --clear
```

* If you already install dependencies. Run bash below to access virtual enviroment
```bash
  pipenv shell
```

* Migration
```bash
  python manage.py migration_generate
  python manage.py migration_run
```

* Seed
```bash
  python manage.py seed_run
```

* Run project
* Create .env file in root folder. Then copy .env.example patse into ,env inside Apis sub folder

```bash
  cd Apis/
  python manage.py runserver
```