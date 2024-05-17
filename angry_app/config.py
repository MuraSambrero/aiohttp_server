import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CELERY_RESULT_BACKEND = os.environ.get(
        "CELERY_RESULT_BACKEND",
        default="redis://localhost:6379/0",
    )

    CELERY_BROKER_URL = os.environ.get(
        "CELERY_BROKER_URL",
        default="redis://localhost:6379/0",
    )
