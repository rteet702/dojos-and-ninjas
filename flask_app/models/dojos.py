from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    def __repr__(self):
        return f'<Dojo> object: {self.name}'

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('d-and-n').query_db(query)
        dojos = []

        for dojo in results:
            dojos.append(cls((dojo)))

        return dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('d-and-n').query_db(query, data)
        return cls(result[0])


    @classmethod
    def add_dojo(cls, data):
        print('adding dojo')
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        connectToMySQL('d-and-n').query_db(query, data)