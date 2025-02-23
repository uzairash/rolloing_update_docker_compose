from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def random_number():
    # change the container number to 2 and run ./script.sh
    return "contianer number is 1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
