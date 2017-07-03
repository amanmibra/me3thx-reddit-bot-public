from firebase import firebase

database = firebase.FirebaseApplication('https://me3thx-reddit-bot.firebaseio.com/')

result = database.get('/', None)


def addID(id_value):
    database.post('/', id_value)
    global result
    result = database.get('/', None)


def checkDatabase(id_value):
    global result
    inDatabase = any(value == id_value for value in result.values())
    return inDatabase
