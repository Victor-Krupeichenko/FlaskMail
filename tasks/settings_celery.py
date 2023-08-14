from celery import Celery
from settings_env import redis_host, redis_port, redis_db
from kombu import Queue

app_celery = Celery(
    "tasks",
    broker=f"redis://{redis_host}:{redis_port}/{redis_db}",
    broker_connection_retry_on_startup=True  # отключает предупреждение
)

app_celery.conf.result_backend = f"redis://{redis_host}:{redis_port}/{redis_db}"
app_celery.conf.worker_concurrency = 6
app_celery.conf.timezone = "Europe/Moscow"

app_celery.conf.task_queues = (
    Queue("email"),
    Queue("reports")
)
