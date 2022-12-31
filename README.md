# Live Chat web application

## Using Flask, Python-Socketio

1. Clone the repo

2. Create a virtualenv

3. Active the virtualenv

4. Install necessary dependencies

```
pip install -r requirements.txt
```

Then, run the flask app by

```
flask run
```

# Docker

```docker
docker build -t live-chat-flask-socketio .

docker tag live-chat-flask-socketio sabbirsobhani/live-chat-flask-socketio

docker push sabbirsobhani/live-chat-flask-socketio
```

# Commands Dockerfile

with gunicorn

```
CMD [ "gunicorn", "--worker-class", "eventlet", "-w", "1", "app:app"]
```

with only/direct eventlet

```
CMD [ "python3", "app.py"]
```

# Thanks

To solve gunicorn with eventlet issue.

1. https://stackoverflow.com/a/72224899/7009215

Enjoy!
