from flask import Flask
import pinata_cannon
app = Flask(__name__)

print(pinata_cannon.test())


@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')