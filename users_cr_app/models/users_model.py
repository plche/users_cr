from users_cr_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, first_name, last_name, email, created_at):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at

    @classmethod
    def getUsers(cls):
        query = "SELECT * FROM users;"
        queryResult = connectToMySQL("users_schema").query_db(query)
        usersList = []
        for user in queryResult:
            usersList.append(User(user["first_name"], user["last_name"], user["email"], user["created_at"]))
        return usersList
    
    @classmethod
    def addUser(cls, newUser):
        query = "INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
        queryResult = connectToMySQL("users_schema").query_db(query, newUser)
        return queryResult