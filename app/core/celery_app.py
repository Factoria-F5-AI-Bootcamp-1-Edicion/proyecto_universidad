from celery import Celery

"""Relación del worker de Celery con el router de nuestra API"""

celery_app = Celery("worker", broker="amqp://guest@queue//")

celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}


