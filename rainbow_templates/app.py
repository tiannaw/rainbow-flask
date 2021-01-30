from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def main():
    return "<h1>Tianna's Rainbow Project</h1>"

@app.route('/red2')
def red():
    colors = red
    return render_template("all_colors.html", colors = colors)
    
@app.route('/orange2')
def orange():
    colors = orange 
    return render_template("all_colors.html", colors = colors)

@app.route('/yellow2')
def yellow():
    colors = yellow
    return render_template("all_colors.html", colors = colors)

@app.route('/green2')
def green():
    colors = green
    return render_template("all_colors.html", colors = colors)

@app.route('/blue2')
def blue():
    colors = blue
    return render_template("all_colors.html", colors = colors)

@app.route('/indigo2')
def indigo():
    colors = indigo
    return render_template("all_colors.html", colors = colors)

@app.route('/violet2')
def violet():
    colors = violet 
    return render_template("all_colors.html", colors = colors)

@app.route('/rainbow')
def all_colors():
    links = ['red', 'orange', 'yellow', 'green', 'blue', ',indigo', 'violet']
    return render_template("rainbow_templates.html", links = links)

















if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
