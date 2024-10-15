# import os
#
# from celery import Celery
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
#
# app = Celery('config')
#
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# app.conf.imports = ('transfer_app.tasks',)
#
# app.autodiscover_tasks()
#
# # Настройка Celery Beat (для запланированных задач)
# # app.conf.beat_schedule = {
# #     'process_recurring_payments': {
# #         'task': 'transfer_app.tasks.process_recurring_payments',
# #         'schedule': 10.0,  # Задача будет выполняться каждые 10 секунд
# #     },
# # }
#
#
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
