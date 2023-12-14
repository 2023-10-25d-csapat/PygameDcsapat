def megjelenítés(tszó, tpk):
  megjelenítés = ''
  for karakter in tszó:
    if karakter in tpk:
      megjelenítés += karakter
    else:
      megjelenítés += '_'
  return megjelenítés
  
def amig(akarsz, tipp, szó):
