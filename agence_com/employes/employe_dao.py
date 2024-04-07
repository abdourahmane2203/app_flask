import database
class EmployeDao:
    connexion = database.connection_db()
    cursor = connexion.cursor()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM employe"
        try:
            EmployeDao.cursor.execute(sql)
            employes = EmployeDao.cursor.fetchall()
            message = 'success'
        except Exception as error:
            employes = []
            message = 'Erreur de récupération des données !' 

        return (message, employes)       