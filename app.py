from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    # Development server; for production use a WSGI server
    app.run(debug=True, host='127.0.0.1', port=5000)
