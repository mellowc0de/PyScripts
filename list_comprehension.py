# Without list comprehension
multiples = []
for x in range(1,11):
  multiples.append(x*7)
print(multiples)

# With list comprehension
multiples = [ x*7 for x in range(1,11)]
print(multiples)

# Sing length with lists
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

# Using modulo with list comprehension
z = [x for x in range(0,101) if x % 3 == 0]
print(z)

# Another list comprehension
def odd_numbers(n):
	return [x for x in range(0, n+1) if x%2 !=0]

print(odd_numbers(10))