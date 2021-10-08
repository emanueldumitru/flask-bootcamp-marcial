from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash('mypass')
print(hashed_pass)

print ( check_password_hash(hashed_pass, 'wrong'))
print ( check_password_hash(hashed_pass, 'mypass'))