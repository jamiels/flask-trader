from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "DATA 602 - Welcome!"

if __name__ == "__main__":
    app.run(host='0.0.0.0') # host='0.0.0.0' needed for docker
	

