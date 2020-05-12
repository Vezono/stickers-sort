nohup python3 ./redis/main.py & python3 ./bot/main.py & gunicorn web.app:app
