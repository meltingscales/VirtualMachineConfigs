import json
import logging
import urllib.request

from flask import jsonify, Flask

from pingn.dao import DAO
from pingn.pingutil import get_config_item, get_config_item_as_bool

app = Flask('pingn')
app.logger.setLevel(logging.INFO)

# Are we the root ping that depends on nothing?
IS_ROOT_PING = get_config_item_as_bool(app, 'ROOT_PING', False)

if not IS_ROOT_PING:
    app.logger.info("This is a child ping server.")
    CHILD_URL = get_config_item(app, 'CHILD_URL')
    CHILD_NAME = get_config_item(app, 'CHILD_NAME')
    CHILD_ENDPOINT = "/{0}".format(CHILD_NAME)
    CHILD_URL_ENDPOINT = CHILD_URL + CHILD_ENDPOINT
else:
    app.logger.info("This is a root ping server.")

APP_NAME = get_config_item(app, 'APP_NAME')
APP_ENDPOINT = "/{0}".format(APP_NAME)

dao: DAO = None
if get_config_item(app, 'PSQL_HOST', None, allow_empty=True):
    app.logger.info("We are also using PostgreSQL for logging.")

    kw = {}
    if get_config_item(app, 'PSQL_PORT', allow_empty=True):
        kw['PSQL_PORT'] = get_config_item(app, 'PSQL_PORT')

    # if adasdfasdf:
    #       kw[asdfasdf] = 'asdfasdfasdf' etc etc

    dao = DAO(app, apphost=APP_NAME, host=get_config_item(app, 'PSQL_HOST', **kw))


@app.route("/")
def index():
    if dao:
        dao.log_event('index', 'got index hit!')

    ret = {"message": "go to " + APP_ENDPOINT}

    if IS_ROOT_PING:
        ret['extra'] = 'also...we are a root ping server :3c'

    return jsonify(ret)


@app.route(APP_ENDPOINT)
def api():
    result = {"message": "hello from " + APP_NAME}

    # If we depend on something, query it
    if not IS_ROOT_PING:
        app.logger.info(f"send GET to child: {CHILD_URL_ENDPOINT}")
        data = {}
        with urllib.request.urlopen(CHILD_URL_ENDPOINT) as url:
            data = json.loads(url.read().decode())

        result.update({f"{CHILD_NAME}_result": data})
    else:
        result['extra'] = 'also...we are a root ping server :3c'

    if dao:
        dao.log_event('api', str(result))

    return jsonify(result)


if __name__ == '__main__':
    h = get_config_item(app, 'HOST', '0.0.0.0')
    p = get_config_item(app, 'PORT', '5000')

    app.logger.info("Starting pingn for {}".format(APP_NAME))

    app.run(host=h,
            port=p,
            debug=True)
