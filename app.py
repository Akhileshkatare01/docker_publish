from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, Dockerized Jenkins!'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000

 
cat requirements.txt 
Flask==2.3.2
