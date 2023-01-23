from passlib.context import CryptContext

myctx = CryptContext(
    schemes=[
        "sha256_crypt",
    ]
)


def hash_telegram_id(telegram_id):
    h = myctx.hash(telegram_id)
    return h
