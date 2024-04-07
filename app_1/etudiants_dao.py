import database

def liste_etudiants():
    connexion = database.connection_db()
    cursor = connexion.cursor()
    sql = "select * from etudiant"
    cursor.execute(sql)

    etudiants = cursor.fetchall()
    cursor.close()

    return etudiants