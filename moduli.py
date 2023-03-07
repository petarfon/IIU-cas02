# modul je fajl koji sadrzi vise funkcija koje ce biti ukljucene u vasoj aplikaciji
# Postoje i predefinisani moduli koji mogu da se instaliraju preko pip package manager-a (npr Django) isto kao i custome module-i (mozete kreirati vase module)

# 1) CORE MODULES
import datetime
from datetime import date
import time
from time import time
import math
import random

# 2) PIP MODULE
# pokrenuti komandu u terminalu 
# pip install camelcase
# instalacija se moze proveriti komandom pip freeze
from camelcase import CamelCase



# 3) import CUSTOM MODULE
#import validator
from validator import validate_jmbg


# 1)
# today = datetime.date.today()
today = date.today()
timestamp = time()

print(today)
print(timestamp)  # menja se svaki put jer se timestamp stalno menja

x = 5.4
print(math.ceil(x))
print(math.floor(x))
x *= -1
print(math.fabs(x))  # aposlutna vrednost
x *= -1
print(math.factorial(math.ceil(x)))

print(math.ceil(random.random()*10))

# 2)
# pip install camelcase -> instaliramo ovo globalno
# pip freeze -> proveravamo sve module koje imamo instalirane
c = CamelCase('of')
print(c.hump('lord of the rings'))

# 3)
jmbg = input('Unesi JMBG: ')
if validate_jmbg(jmbg):
    print('Ispravan jmbg!')
else:
    print('jmbg nije ispravan!')
