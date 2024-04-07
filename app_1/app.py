from flask import Flask, render_template
import etudiants_dao

app = Flask(__name__)

@app.route("/")
def home():
    titre_page = "Collège cumberland"
    nom = "Stéphane Labrie"

    return render_template("index.html", nom=nom, page_title=titre_page)

@app.route("/about")
def about():
    description = """
                    Une carrière en marketing numérique à votre portée !
                    Le monde du marketing en ligne connaît une croissance spectaculaire et constante, et les possibilités de carrière se multiplient à un rythme tout aussi soutenu. Grâce aux connaissances et aux compétences de pointe acquises dans le cadre de notre Attestation d’études collégiales (AEC) en Marketing numérique, vous serez en mesure d’accéder à des postes aussi recherchés que ceux d’adjoint au marketing, de spécialiste du marketing numérique et de coordonnateur du marketing numérique. Vous serez également préparé à entrer dans des domaines spécifiques tels que l’optimisation des moteurs de recherche (SEO), la gestion des médias sociaux, le marketing de contenu, le marketing par courriel, l’analyse Web, et plus encore !

                    Le programme comprend un total de 900 heures de cours sur une période de 16 mois, avec un maximum de 20 heures de cours par semaine.

                    Des aides financières, notamment des prêts et des bourses, peuvent être disponibles auprès du gouvernement provincial du Québec pour vous aider à financer vos études. L’admissibilité est déterminée par le MEES (ministère de l’Éducation de l’Enseignement supérieur).
                  """
    return render_template("about.html", desc = description)

@app.route("/test")
def test_majeur():
    age = 18
    nom = "Maxime St-Pierre"
    
    etudiants = [
        {"nom":"Labrie", "prenom":"Stéphane", "age":40},
        {"nom":"St-Piere", "prenom":"Maxime", "age":27},
        {"nom":"Diallo", "prenom":"Ousman", "age":37},
        {"nom":"Issa", "prenom":"Aamadou", "age":29},
    ]
    
    return render_template(
                    "test_majeur.html", 
                    age=age, 
                    nom=nom,
                    etudiants=etudiants
                    )

@app.route("/etudiants")
def liste_etudiants():
    etudiants = etudiants_dao.liste_etudiants()
    
    return render_template('liste_etudiants.html', etudiants)

