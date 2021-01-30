from flask import Flask, render_template, current_app as current_app

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Tianna's Rainbow Project</h1>"

@app.route('/red', methods = ['GET'])
def red():
    return render_template("red.html")
    
@app.route('/orange', methods = ['GET'])
def orange():
    return render_template("orange.html")

@app.route('/yellow', methods = ['GET'])
def yellow():
    return render_template("yellow.html")

@app.route('/green', methods = ['GET'])
def green():
    return render_template("green.html")

@app.route('/blue', methods = ['GET'])
def blue():
    return render_template("blue.html")

@app.route('/indigo', methods = ['GET'])
def indigo():
    return render_template("indigo.html")

@app.route('/violet', methods = ['GET'])
def violet():
    return render_template("violet.html")








if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')