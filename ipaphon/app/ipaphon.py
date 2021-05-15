"""
All of the routes of the app can be found in this module:

Available routes:
 - upload_file: A user can use this route to send files
   to the server. All files are assumed to be text files.
"""
import io
from typing import Text, Union

import chardet
import epitran
from flask import flash, redirect, render_template, request
from flask.helpers import send_file
from flask.wrappers import Response
from werkzeug.utils import secure_filename

from . import main


@main.route("/", methods=["GET", "POST"])
def upload_file() -> Union[Text, Response]:
    """
    Handle user uploads and render the index page.

    Returns
    -------
    Union[Text, Response]
        In case of a response to a user upload,
        the processed file or the index page, otherwise.
    """
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
            # We handle the file transfer in memory,
            # instead of using a temporary file
            ipa = io.BytesIO(epi.transliterate(text).encode())
            ipa.seek(0)
            return send_file(
                ipa,
                mimetype="text/plain",
                as_attachment=True,
                attachment_filename=secure_filename(file.filename + ".ipa"),
            )
    return render_template("index.html")
