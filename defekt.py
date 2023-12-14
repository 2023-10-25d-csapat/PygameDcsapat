def megjelenítés(tszó, tpk):
  megjelenítés = ''
  for karakter in tszó:
    if karakter in tpk:
      megjelenítés += karakter
    else:
      megjelenítés += '_'
  return megjelenítés
  
def amig(akarsz, tipp, szó):
  while True:
        if akarsz:
            _1 =input("kaparj ide valamit: ")
            tipp.append(_1)
            print(megjelenítés(szó, tipp))
            if megjelenítés(szó, tipp) == szó:
                print("Gratulálok! Találtad a titkos szót:", szó)
                break
