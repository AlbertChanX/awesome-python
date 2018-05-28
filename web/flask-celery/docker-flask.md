
## deploy with docker

### Gunicorn+Gevent --> Flask
```
pip install gunicorn gevent
```

* app.py
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello docker&flask'

if __name__ == '__main__':
    app.run(debug=True)
```

* vim `gunicorn.conf.py`

```
workers = 5    
# 定义同时开启的处理请求的进程数量，根据网站流量适当调整
worker_class = "gevent"   
# 采用gevent库，支持异步处理请求，提高吞吐量
bind = "0.0.0.0:8888"    
# 监听IP放宽，以便于Docker之间、Docker和宿主机之间的通信

```
* run 
```
gunicorn app:app -c gunicorn.conf.py
```

### run with docker
> 接下来是配合supervisor将应用部署到主机上，
> supervisor的主要作用是监控和修复应用的运行状态。
> 现在，将应用部署到Docker中，这个任务就交给Docker来实现(使用容器云平台例如`kubernetes`可以更好地实现这个功能)。

* vim Dockerfile

```
FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]

```

* build image

```
sudo docker build -t '{project/image name}' .
```

* run in a daemon way
```
sudo docker run **-d** -p 8888:8888 --name test-flask-1 {image-name}
```

## Refer
[用Docker部署Flask应用 - 简书](https://www.jianshu.com/p/5b09394bebfe)