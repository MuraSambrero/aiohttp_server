from celery import Celery
import hashlib
from config import Config

celery_app = Celery(
    "hash", backend=Config.CELERY_RESULT_BACKEND, broker=Config.CELERY_BROKER_URL
)


@celery_app.task
def hash_calc(hash_string: str):
    return hashlib.sha256(hash_string.encode()).hexdigest()
