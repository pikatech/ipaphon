[![Works with Python 3.6+](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-informational.svg)](https://www.python.org/downloads/)[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/pikatech/ipaphon/blob/main/LICENSE)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# ipaphon - text to IPA

A skeleton Flask app demonstrating how to process uploaded files.

It will transliterate uploaded text files into IPA (International Phonetic Alphabet).

## Run it with a production server

`waitress-serve --call 'ipaphon.main:wsgi'`

## Run it with the integrated development server

```bash
export FLASK_APP=ipaphon.wsgi
export FLASK_ENV=development
flask run
```

## Getting started with web development

https://getbootstrap.com/docs/5.0/getting-started/introduction/

https://getbootstrap.com/docs/5.0/forms/form-control/

https://flask.palletsprojects.com/en/2.0.x/

https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
