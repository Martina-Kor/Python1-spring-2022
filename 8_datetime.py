from datetime import datetime, timedelta

apolloStart = datetime(1969, 7, 16, 14, 32)
print(apolloStart)

datum_narozeni = datetime(1974, 8, 16)
print(datum_narozeni)
print(datum_narozeni.weekday())
print(datum_narozeni.isoweekday())

# funkce isoformat() # T mezi datum a čas

# funkce strftime(), aneb z data na řetězec (formatting time)
print(apolloStart.isoweekday())

print(apolloStart.strftime("%d. %m. %Y, %H:%M"))
print(apolloStart.strftime("%A"))


import locale
# locale.setlocale(locale.LC_TIME, 'cs_CZ.UTF-8') # iOS
locale.setlocale(locale.LC_TIME, 'cz.UTF-8') # Windows?

print(apolloStart.strftime("%A"))

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

# funkce strptime(), aneb z řetězce na datum (parse time)

retezec = "21. 7. 1069, 18:54"

pristani2 = datetime.strptime(retezec, "%d. %m. %Y, %H:%M")
print(pristani2)

#start - stop, spočítej délku mise Apolla 11
mise = pristani2 - apolloStart
print(mise)


# včerejší datum

dnes = datetime.today()
vcera = dnes - timedelta(days=1)
print(vcera.strftime("%d. %m. %Y"))

# kolik dní jsem na zemi
# dnes - datum narozeni
delka_zivota = dnes - datum_narozeni
print(delka_zivota)



