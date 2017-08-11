from flask import Flask
@app.route('/')

def index():
    return "DATA 602 - Welcome!"
	
if __name__ == "__main__":
    app.run(host="0.0.0.0")
	

