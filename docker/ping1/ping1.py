from flask import jsonify

from pyms.flask.app import Microservice

ms = Microservice(path=__file__)
app = ms.create_app()


@app.route("/ping1")
def example():
    return jsonify({"message": "hello from server1"})


if __name__ == '__main__':
    app.run()