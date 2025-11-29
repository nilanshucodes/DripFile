import os
import time
import base64
import json
import random
import string
from flask import Flask, request, send_file, render_template

app = Flask(__name__)

# Vercel-safe temp folder
UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

MAX_SIZE = 25 * 1024 * 1024  # 25 MB
EXPIRY_SECONDS = 15 * 60     # 15 minutes


def random_id(n=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


def encode(data: dict):
    return base64.urlsafe_b64encode(json.dumps(data).encode()).decode()


def decode(token: str):
    try:
        return json.loads(base64.urlsafe_b64decode(token.encode()).decode())
    except:
        return None


@app.errorhandler(413)
def file_too_large(e):
    return "File is too large. Maximum allowed size is 25 MB.", 413


@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":

        if "file" not in request.files:
            return render_template("index.html", error="No file selected", link=None)

        file = request.files["file"]

        if file.filename == "":
            return render_template("index.html", error="No file selected", link=None)

        filename = file.filename
        file_id = random_id()

        # Temporary path in /tmp
        saved_name = f"{file_id}_{filename}"
        path = os.path.join(UPLOAD_FOLDER, saved_name)
        file.save(path)

        # Encode metadata inside the link
        token = encode({
            "name": filename,
            "stored": saved_name,
            "time": time.time()
        })

        share_link = request.host_url + "d/" + token

        return render_template("index.html", link=share_link, error=None)

    return render_template("index.html", link=None, error=None)


@app.route("/d/<token>")
def download(token):
    info = decode(token)
    if not info:
        return "Invalid or expired link.", 400

    # Check expiry
    if time.time() - info["time"] > EXPIRY_SECONDS:
        return "This link has expired.", 410

    stored_path = os.path.join(UPLOAD_FOLDER, info["stored"])
    if not os.path.exists(stored_path):
        return "File removed or unavailable.", 410

    return send_file(stored_path, as_attachment=True, download_name=info["name"])
