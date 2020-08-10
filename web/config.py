from os import environ as e

creator = int(e["ADMIN_ID"])
token = e['TELEGRAM_TOKEN']
database = e['MONGO_LINK']
