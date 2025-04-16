from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    with open("log.txt", "a") as f:
        f.write(f"{ip}\n")
    return f"Twoje IP zostało zapisane: {ip}"