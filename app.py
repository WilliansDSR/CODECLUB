from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "codeclub123"

@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token == VERIFY_TOKEN:
        return challenge

    return "Token inválido", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print(data)
    return "ok", 200

 @app.route("/")
def home():
    return "CodeClub Bot Online"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
