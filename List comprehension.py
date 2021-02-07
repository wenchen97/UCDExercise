squares = [i**2 for i in range(10)]
print(squares)

matrix = [[col for col in range (5)] for row in range(0,5)]
for row in matrix:
    print(row)

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# new_fellowship = [member for member in fellowship if len(member)>=7]
# print(new_fellowship)

new_fellowship = [member if len(member)>=7 else "" for member in fellowship ]
print(new_fellowship)

new_fellowship = {member:len(member) for member in fellowship}
print(new_fellowship)

#fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
#fellow1 = [member for member in fellowship if len(member) >= 7]
#fellow2 = (member for member in fellowship if len(member) >= 7)

result = (num for num in range(31))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
for value in result:
    print(value)


#lengths = (len(person) for person in lannister)
#for value in lengths:
    #print(value)

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""
    for person in input_list:
        yield len(person)

for value in get_lengths("lannister"):
    print(value)


