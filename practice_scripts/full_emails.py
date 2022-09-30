def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result

print(full_emails([("adamalcala1988@gmail.com", "Adam Alcala")]))