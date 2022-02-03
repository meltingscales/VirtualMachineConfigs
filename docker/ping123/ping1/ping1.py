from flask import jsonify

from pyms.flask.app import Microservice

ms = Microservice(path=__file__)
app = ms.create_app()


@app.route("/")
def index():
    return jsonify({"message": "go to /ping1"})


@app.route("/ping1")
def ping1():
    return jsonify({"message": "hello from "+app.config.get('APP_NAME')})


if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),
            port=app.config.get('PORT'))
