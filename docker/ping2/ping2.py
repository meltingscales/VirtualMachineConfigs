from multiprocessing.sharedctypes import Value
import os
from flask import jsonify
import urllib.request
import json

from pyms.flask.app import Microservice

ms = Microservice(path=__file__)
app = ms.create_app()


def get_ping1_url() -> str:
    result = None
    # prefer env vars for ping1_url
    result = os.environ.get('PING1_URL', None)
    if result:
        print("Using PING1_URL from os.environ: "+result)
        return result

    # then try app.config
    result = app.config.get('PING1_URL', None)
    if result:
        print("Using PING1_URL from app.config: "+result)
        return result

    # check if it's empty
    raise ValueError("You must set 'PING1_URL' in config.yml or env vars!"
                     "HALTING! This service depends on ping1!")


PING1_URL = get_ping1_url()


@app.route("/")
def index():
    return jsonify({"message": "go to /ping2"})


@app.route("/ping2")
def ping2():

    result = {"message": "hello from "+app.config.get('APP_NAME')}

    data = {}
    with urllib.request.urlopen(PING1_URL+"/ping1") as url:
        data = json.loads(url.read().decode())

    result.update({"ping1_result": data})

    return jsonify(result)


if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),
            port=app.config.get('PORT'))
