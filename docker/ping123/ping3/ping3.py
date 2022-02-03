from multiprocessing.sharedctypes import Value
import os
from flask import jsonify
import urllib.request
import json

from pyms.flask.app import Microservice

ms = Microservice(path=__file__)
app = ms.create_app()


def get_ping2_url() -> str:
    result = None
    # prefer env vars for PING2_URL
    result = os.environ.get('PING2_URL', None)
    if result:
        print("Using PING2_URL from os.environ: "+result)
        return result

    # then try app.config
    result = app.config.get('PING2_URL', None)
    if result:
        print("Using PING2_URL from app.config: "+result)
        return result

    # check if it's empty
    raise ValueError("You must set 'PING2_URL' in config.yml or env vars!"
                     "HALTING! This service depends on ping1!")


PING2_URL = get_ping2_url()


@app.route("/")
def index():
    return jsonify({"message": "go to /ping3"})


@app.route("/ping3")
def ping3():

    result = {"message": "hello from "+app.config.get('APP_NAME')}

    data = {}
    with urllib.request.urlopen(PING2_URL+"/ping1") as url:
        data = json.loads(url.read().decode())

    result.update({"ping2_result": data})

    return jsonify(result)


if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),
            port=app.config.get('PORT'))
