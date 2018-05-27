# coding:utf-8
# https://blog.csdn.net/junchen19/article/details/54025897
# https://www.cnblogs.com/klb561/p/8688229.html
from flask import Flask, render_template, jsonify, url_for
from celery import Celery
import logging

import time
 
app = Flask('app')

celery = Celery('app')
celery.config_from_object('config')
celery.conf.update(app.config)

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
@celery.task(bind=True)
def long_task(self):
    while True:
        print("sleep")
        time.sleep(15)
        
    return True

@app.route('/longtask', methods=['GET', 'POST'])
def longtask():
    task = long_task.apply_async()
    return jsonify({}), 200
    
import gevent.pywsgi

if __name__ == '__main__':   
    gevent_server = gevent.pywsgi.WSGIServer(('localhost', 9999), app)
    gevent_server.serve_forever()

#  celery -A application.celery worker -l info