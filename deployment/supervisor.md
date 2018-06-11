
## supervisor
```
yum/pip install suervisor
```

`help`
```
supervisord -h
```

`start`
```
supervisord -c /etc/{supervisor}/supervisord.conf
```
* vim /etc/supervisord.d/program.ini
```
supervisorctl reread
supervisorctl reload
```

## issue
> Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

```
$ systemctl daemon-reload
$ service docker restart
$ service docker status (should see active (running))
$ docker run hello-world
```

## Reference
1. [Supervisor/initscripts: User-contributed OS init scripts for Supervisor](https://github.com/Supervisor/initscripts)
2. [iptables命令_Linux iptables 命令用法详解：Linux上常用的防火墙软件](http://man.linuxde.net/iptables)
3. [云服务器 ECS Linux CentOS 7 下使用iptables服务_网络问题_操作运维 Linux_常见问题_云服务器 ECS-阿里云](https://help.aliyun.com/knowledge_detail/41319.html?spm=5176.11065259.1996646101.searchclickresult.7ff15ba8a8eC9F)