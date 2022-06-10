sentence = input("Write any sentence: ").lower().strip()

amount_a = sentence.count('a')
first_a = sentence.find('a') + 1
last_a = sentence.rfind('a') + 1

print(f'The letter A appears {amount_a} times.')
print(f'The first letter A appears in position {first_a}.')
print(f'The last letter A appears in position {last_a}.')
print('Obs: Position 0 means that there are no letter A in the sentence.')