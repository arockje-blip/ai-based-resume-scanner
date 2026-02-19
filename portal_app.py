from pathlib import Path
from flask import Flask, redirect

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    html_path = BASE_DIR / "portal_index.html"
    if html_path.exists():
        with open(html_path, "r", encoding="utf-8") as file:
            return file.read()
    return "<h1>Role Portal</h1><p>portal_index.html not found.</p>", 404


@app.route("/go/employer", methods=["GET"])
def go_employer():
    return redirect("http://127.0.0.1:5001/")


@app.route("/go/job-seeker", methods=["GET"])
def go_job_seeker():
    return redirect("http://127.0.0.1:5000/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
