from tornado_json.requesthandlers import APIHandler
import json
from tornado_json import schema
from tornado.escape import json_decode
# https://github.com/Julian/jsonschema
# https://github.com/hfaran/Tornado-JSON/blob/master/demos/helloworld/helloworld/api.py


class BaseHandler(APIHandler):
    def get_json_argument(self, name, default=None):
        args = json_decode(self.request.body)
        name = to_unicode(name)
        if name in args:
            return args[name]
        elif default is not None:
            return default
        else:
            raise MissingArgumentError(name)


class IndexHandler(APIHandler):
    @schema.validate(input_schema={
        "type": "object",
        "properties": {
                "test": {"type": "string"},
                # "body": {"type": "string"},
                # "index": {"type": "number"},
        }
    },
        # output_schema=...
    )
    def post(self):
        """I am the public API documentation of this route"""
        try:
            data = json_decode(self.request.body)
            print(data)
        except Exception as e:
            print(e)
        return data['test']


class TestHandler(APIHandler):
    """docstring for TestHandler"""

    def get(self):
        pass
