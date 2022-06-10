fullname = input("Hello! What's your fullname? ")
print('Nice to meet you!')

listname = fullname.split()
firstname = listname[0].title()
lastname = listname[-1].title()

print(f'Your fist name is {firstname}.')
print(f'Your last name is {lastname}.')