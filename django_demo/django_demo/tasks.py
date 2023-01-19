from celery import Celery
import os
app = Celery('tasks', broker='redis://redis:6379', backend='redis://redis:6379')

@app.task
def hello(caller_host):
    return f"""Hi {caller_host}! This is {os.environ.get("HOSTNAME", 'celery_worker_hostname')}."""