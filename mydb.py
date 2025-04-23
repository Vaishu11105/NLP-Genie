import json

class Database:
    def add_data(self,email,password):
          
        with open('db.json','r') as rf:
            database = json.load(rf)

        if email in database:
            return 0
        else:
            database[email] = password
            with open('db.json','w') as wf:
                json.dump(database,wf)
            return 1        

    def validate_credentials(self,email,password):

        with open('db.json','r') as rf:
            database = json.load(rf)

        if email in database:
            if database[email]==password:
                return True 
            else:
                return False

        return False


Database()                     