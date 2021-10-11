#secure_check.py

from user import User

users = [
    User(1, 'Jose', 'mypassword'),
    User(2, 'Mimi', 'secret')
]

username_table = {u.username : u for u in users}
userid_table = {u.id : u for u in users}

# Authenticate
def authenticate(username, password):
    # check if user exists and if so return the user

    user = username_table.get(username)
    if user and password == user.password:
        return user

# Identity
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)



