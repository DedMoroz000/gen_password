import random

vowels = 'euyioaEYUIOA'
consonants = 'qwrtpsdfghjklzxcvbnmQWRTPSDFGHHJKLZXCVBNM'
numbers = '1234567890'
symbols = "№+=-!*/@"

for i in range(3):
    password += random.choice(consonants)
    password += random.choice(vowels)

for i in range(2):
    password += random.choice(numbers)

for i in range(2):
    password += random.choice(symbols)
print(password)
