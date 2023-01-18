
def user(fname, lname):
    username = fname[0].lower() + lname.lower()
    email = username + '@gmail.com'
    
    print('First name: {} \nLast name: {} \nUsername: {} \nEmail: {} \n'.format(fname, lname, username, email))

print(user('Adam', 'Alcala'))