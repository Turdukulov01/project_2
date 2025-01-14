# task_manager/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tast_manager.settings')

app = Celery('tast_manager')

# Чтение конфигурации из settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач в приложениях
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    
app.conf.update(
    broker_connection_retry_on_startup=True
)

