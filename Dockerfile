FROM python:3.12-slim

WORKDIR /code

COPY . /code/

RUN pip install pipenv && pipenv install
RUN pip install --upgrade setuptools

WORKDIR /code/Apis

EXPOSE 3000

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:3000"]