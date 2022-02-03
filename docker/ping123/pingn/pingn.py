from pingutil import get_config_item
from flask import jsonify
import urllib.request
import json

from pyms.flask.app import Microservice

ms = Microservice(path=__file__)
app = ms.create_app()

# Are we the root ping that depends on nothing?
IS_ROOT_PING = get_config_item(app, 'IS_ROOT_PING', False)

if not IS_ROOT_PING:
    CHILD_URL = get_config_item(app, 'CHILD_URL')
    CHILD_NAME = get_config_item(app, 'CHILD_NAME')
    CHILD_ENDPOINT = "/{0}".format(CHILD_NAME)
    CHILD_URL_ENDPOINT = CHILD_URL + CHILD_ENDPOINT

APP_NAME = get_config_item(app, 'APP_NAME')
APP_ENDPOINT = "/{0}".format(APP_NAME)


@app.route("/")
def index():
    return jsonify({"message": "go to " + APP_ENDPOINT})


@app.route(APP_ENDPOINT)
def pingn():
    result = {"message": "hello from " + app.config.get('APP_NAME')}

    # If we depend on something, query it
    if not IS_ROOT_PING:
        print(f"send GET to child: {CHILD_URL_ENDPOINT}")
        data = {}
        with urllib.request.urlopen(CHILD_URL_ENDPOINT) as url:
            data = json.loads(url.read().decode())

        result.update({f"{CHILD_NAME}_result": data})

    return jsonify(result)


if __name__ == '__main__':
    h = get_config_item(app, 'HOST', '0.0.0.0')
    p = get_config_item(app, 'PORT')

    app.run(host=h,
            port=p)
