first_name = input('First name: ')
last_name = input('Last name: ')

def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag(first_name, last_name))