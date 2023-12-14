import random

def megjelenítés(tszó, tpk):
  megjelenítés = ''
  for karakter in tszó:
    if karakter in tpk:
      megjelenítés += karakter
    else:
      megjelenítés += '_'
  return megjelenítés

l = ['Debrecen', 'Szeged', 'Csaba', 'Eger']
szó = random.choice(l)
tipp = []
akarsz = input("Szeretnél Játszani ? (I/N)")
if akarsz.lower() == "i" and akarsz.isalpha():
    print("=-=-=-=-=-= The Akasztófa =-=-=-=-=-=")
else:
   print("Ez van")

while True:
  if akarsz:
    _1 =input("kaparj ide valamit: ")
    tipp.append(_1)
    print(megjelenítés(szó, tipp))
    if megjelenítés(szó, tipp) == szó:
      print("Gratulálok! Találtad a titkos szót:", szó)
      break
