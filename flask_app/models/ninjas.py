from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    def __repr__(self):
        return f'<Ninja> object: {self.id}, {self.first_name}, {self.last_name}'

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('d-and-n').query_db(query)
        ninjas = []

        for dojo in results:
            ninjas.append(cls((dojo)))

        return ninjas

    @classmethod
    def add_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo)s);"
        connectToMySQL('d-and-n').query_db(query, data)

    @classmethod
    def get_by_dojo(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        results = connectToMySQL('d-and-n').query_db(query, data)
        ninjas = []

        for ninja in results:
            ninjas.append(cls(ninja))

        return ninjas