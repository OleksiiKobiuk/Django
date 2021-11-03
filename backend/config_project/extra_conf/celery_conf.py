CELERY_BROKER_URL = "redis://redis:6379/0" #стандартний порт БД redis
CELERY_BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}

CELERY_RESULT_BACKEND = "redis://redis:6379/0"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
