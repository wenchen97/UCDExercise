flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
for person in flash:
    print(person)
superhero = iter(flash)
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

small_value = iter(range(3))
print(next(small_value))
print(next(small_value))
print(next(small_value))
for num in range(3):
    print (num)
googol = iter(range(10**100))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

values = range(10,21)
print(values)
values_list = list(values)
print(values_list)
values_sum = sum(values)
print(values_sum)