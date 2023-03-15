from celery import Celery
from flask_mail import Message
from ext import mail


def send_mail(recipients, subject, body):
    message = Message(subject=subject, recipients=[recipients], body=body)
    mail.send(message)
    print('邮件发送成功')


def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    app.celery = celery

    # 下面添加任务
    celery.task(name='send_mail')(send_mail)

    return celery



