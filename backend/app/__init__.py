from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='../frontend/build')

@app.route('/&lt;path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)