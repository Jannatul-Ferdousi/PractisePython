# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [i if len(i)>=7 else '' for i in fellowship]

# Print the new list
print(new_fellowship)
