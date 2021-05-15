import os

import chardet
import epitran
from flask import (
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask.globals import current_app
from werkzeug.utils import secure_filename

from . import main


@main.route("/uploads/<name>")
def download_file(name):
    return send_from_directory(current_app.config["DOWNLOAD_FOLDER"], name)


@main.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file:
            raw_text = file.read()
            encoding = chardet.detect(raw_text)
            text = raw_text.decode(encoding["encoding"])
            epi = epitran.Epitran("deu-Latn")
            ipa = epi.transliterate(text)
            filename = secure_filename(file.filename + ".ipa")
            with open(
                os.path.join(current_app.config["DOWNLOAD_FOLDER"], filename), "wt"
            ) as ipafile:
                _ = ipafile.write(ipa)
            return redirect(url_for("main.download_file", name=filename))
    return render_template("index.html")
