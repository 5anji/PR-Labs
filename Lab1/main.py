from flask import Flask, request

app = Flask(__name__)

@app.route('/hello', methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return {"message" : "World!"}
    elif request.method == "POST":
        payload = request.json
        for key, value in payload.items():
            print(f"{key} : {value}")
        return "confirmation"


app.run()
