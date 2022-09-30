def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for elem in elements:
		# Does this element belong in the resulting list?
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(elem)
		# Increment i
		i += 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

# Skip elements using enumerate
def skip_other_elements(elements):
  other_list =[]
  i = 0
  for i, elem in enumerate(elements):
    if i % 2 == 0:
      other_list.append(elem)
  
    return other_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']