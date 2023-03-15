from App import create_app
import os

env = os.environ.get('FLASK_ENV', default='develop')
app = create_app(env)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
