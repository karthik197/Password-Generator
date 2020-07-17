import random
from string import digits #0-9
from string import punctuation #!@#$%^&)()[]{}|*\/'"_-+~`
from string import ascii_letters #a-z and A-Z
symbols=ascii_letters+punctuation+digits
secure_random=random.SystemRandom()
#to generate password of length 10 
password=''.join(secure_random.choice(symbols)for i in range(10))
print(password)