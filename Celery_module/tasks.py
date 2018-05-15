# coding:utf-8
# tasks.py
# https://blog.csdn.net/apple9005/article/details/54430104
# https://blog.csdn.net/win_turn/article/details/60658525
import time
from celery import Celery, platforms
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost:6379/0')
platforms.C_FORCE_ROOT = True      # 用户解决root用户无法启动worker的问题

@app.task
def send(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')

# 实际上启动的是Worker，如果要放到后台运行，可以扔给supervisor。
# celery -A tasks worker --loglevel=info
# 启动worker，绑定flower监控并设置监控端口
# https://github.com/mher/flower
# celery flower -A tasks --address=127.0.0.1 --port=8083

# Celery 中启动定时任务有两种方式，1在配置文件中指定; 2在程序中指定。
# (1)
# app.conf.beat_schedule = {
#     'send-every-10-seconds': {
#         'task': 'tasks.send',
#         'schedule': 10.0,
#         'args': ('Hello World', )
#     },
# }
# 可以通过在配置文件中编写 beat_schedule 属性，来配置周期性任务，
# 上面的示例配置了一个每十秒执行一次的周期任务，任务为 tasks.send，
# 参数为 'Hello World'。当然你也可以将这个配置写到单独的配置文件中进行读取。
# 这种配置的方式可以支持多个参数，

# 2
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)


# if __name__ == '__main__':
#      # from tasks import sendmail
#      send.delay(dict(to='celery@python.org'))
