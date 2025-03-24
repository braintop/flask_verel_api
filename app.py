from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return {'message': 'Hello World'}

# Remove the if __name__ == '__main__' block for Vercel deployment
# Keep it only for local development
if __name__ == '__main__':
    app.run(debug=True, port=5001)