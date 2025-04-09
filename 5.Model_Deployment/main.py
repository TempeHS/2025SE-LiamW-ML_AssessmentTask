from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import jsonify
from flask import make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import requests
from flask_wtf import CSRFProtect
from flask_csp.csp import csp_header
import random
import dataManagement as dbHandler
import export_import as exporti
import test_import as testi


# Generate a unique basic 16 key: https://acte.ltd/utils/randomkeygen
app = Flask(__name__)
app.secret_key = b"_53oi3uriq9pifpff;apl"
csrf = CSRFProtect(app)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour", "1 per second"],
    storage_uri="memory://",
)

# Redirect index.html to domain root for consistent UX
@app.route("/index", methods=["GET"])
@app.route("/index.htm", methods=["GET"])
@app.route("/index.asp", methods=["GET"])
@app.route("/index.php", methods=["GET"])
@app.route("/index.html", methods=["GET","POST"])
def root():
    return redirect("/", 302)


@app.route("/", methods=["POST", "GET"])
@csp_header(
    {
        # Server Side CSP is consistent with meta CSP in layout.html
        "base-uri": "'self'",
        "default-src": "'self'",
        "style-src": "'self'",
        "script-src": "'self'",
        "img-src": "'self' data:",
        "media-src": "'self'",
        "font-src": "'self'",
        "object-src": "'self'",
        "child-src": "'self'",
        "connect-src": "'self'",
        "worker-src": "'self'",
        "report-uri": "/csp_report",
        "frame-ancestors": "'none'",
        "form-action": "'self'",
        "frame-src": "'none'",
    }
)

def index():
    if request.method == "GET":
        return render_template("/index.html")
    if request.method == "POST":
        entry = []
        popularity = request.form["popularity"]
        project = request.form["project"]
        entry.append(popularity)
        entry.append(project)
        output = 'output'
        return render_template("/index.html", value = 'output')
    return render_template("/index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
