from flask import Flask, request


class MyMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # code untuk middleware
        response = self.app(environ, start_response)
        return response


app = Flask(__name__)

# menambahkan middleware pada Flask
app.wsgi_app = MyMiddleware(app.wsgi_app)

# Route untuk contoh


@app.route('/')
def hello_world():
    return 'Hello, World!'
