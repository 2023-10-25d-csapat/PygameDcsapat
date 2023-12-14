import random
from defekt import *

l = ['Debrecen', 'Szeged', 'Csaba', 'Eger']
szó = random.choice(l)
tipp = []
akarsz = input("Szeretnél Játszani ? (I/N)")
if akarsz.lower() == "i" and akarsz.isalpha():
    print("=-=-=-=-=-= The Akasztófa =-=-=-=-=-=")
    amig(akarsz, tipp, szó)
else:
   print("(T_T)")
