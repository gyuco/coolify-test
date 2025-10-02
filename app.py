from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
import logging

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# Abilita logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    app.logger.info(f"Request from: {request.remote_addr}")
    app.logger.info(f"Headers: {dict(request.headers)}")
    return "Hello World"

@app.route('/health')
def health():
    return "OK", 200