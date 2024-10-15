import uuid

from yookassa import Configuration


def setup_yandex_config(account_id, secret_key):
    Configuration.account_id = account_id
    Configuration.secret_key = secret_key
    return Configuration


def generate_payment_id(amount):
    return str(uuid.uuid4())[:36] + str(int(amount))
