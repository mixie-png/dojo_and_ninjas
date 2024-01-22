# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the ninja table from our database
class Ninja:
    DB = "dojos_and_ninjas"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    # Now we use class methods to query our database
    # READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of ninjas
        ninjas = []
        # Iterate over the db results and create instances of ninjas with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    # READ - get ninjas by dojo_id
    @classmethod
    def get_ninjas_by_dojo(cls, dojo_id):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, {"dojo_id": dojo_id})

        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))

        return ninjas

    # CREATE
    @classmethod
    def add(cls, data):
        # prepared statement to prevent SQL injection
        query = """
            INSERT INTO ninjas (first_name,last_name,age,dojo_id)
    	    VALUES (%(fname)s,%(lname)s,%(age)s,%(dojos)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result