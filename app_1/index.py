from flask import Flask, render_template
#from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    name = "Abdourahmane Diallo"
    return render_template("home.html", name=name)

@app.route("/about2")
def about():
    return "<h2> About our class </h2>"

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return """  <h2> Login </h2>
                <input type="text" placeholder="Votre mail SVP" /> <br><br>
                <input type="text" placeholder="Votre mot de passe SVP" /> <br><br>
                <input type="button" value="Se connecter" /> <br><br>
            """