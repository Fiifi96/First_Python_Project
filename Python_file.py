from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template():
    return render_template("template.html")

@app.route("/H")
def Home():
    return render_template("Home.html")    
    
@app.route("/about")
def about():
    return render_template("about.html")

    
if __name__ == "__main__":
    app.run(debug=True)