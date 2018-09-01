from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():

    nums = [random.randint(0, 100) for i in range(10)]

    return """Hello World!
	
	Here are your lucky numbers: """ + str(nums)
