import json
import tornado.ioloop
from tornado_json.routes import get_routes
from tornado_json.application import Application
# from handler import IndexHandler
# https://shuhm-gh.github.io/2017/04/28/network-web-tornado%E5%A4%84%E7%90%86post%E8%AF%B7%E6%B1%82%E7%9A%84json%E6%95%B0%E6%8D%AE/
# http://tornado-zh.readthedocs.io/zh/latest/guide/security.html
def main():
    import hello
    routes = get_routes(hello)
    print("Routes\n======\n\n" + json.dumps(
        [(url, repr(rh)) for url, rh in routes],
        indent=2)
    )
    application = Application(routes=routes, settings={})

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
