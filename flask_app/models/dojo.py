# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the dojo table from our database
class Dojo:
    DB = "dojos_and_ninjas"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.ninjas = []

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM dojos;"""
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            new_dojo = cls(dojo)
            dojos.append( new_dojo )
        return dojos

    # READ - read a row/record in the data base
    @classmethod
    def show_one(cls, id):
        query = """SELECT * FROM dojos WHERE id = %(id)s;"""
        result = connectToMySQL(cls.DB).query_db(query, {"id" : id})
        # one_dojo = cls(result[0])
        # return one_dojo

        # Check if result is not empty before accessing the first element
        if result:
            one_dojo = cls(result[0])
            return one_dojo
        else:
            return None  # or handle the case where the dojo with the given id is not found

    # CREATE
    @classmethod
    def add(cls, data):
        query = """
            INSERT INTO dojos (name)
    	    VALUES (%(name)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result