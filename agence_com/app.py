from flask import Flask, render_template
from employes.employe_dao import EmployeDao

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")    
def services():
    return render_template("services.html")

@app.route("/employes")    
def employes():
    (message, employes) = EmployeDao.get_all()
    
    for employe in employes:
        print(employe[0])
    return render_template("liste_employes.html", message=message,employes=employes)