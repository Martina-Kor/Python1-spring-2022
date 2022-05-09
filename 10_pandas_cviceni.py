

# https://stage.kodim.cz/kurzy/python-data-1/python-pro-data-1/zakladni-dotazy/excs
""" Datový soubor obsahuje následující sloupečky

jméno - křestní jméno
četnost - počet obyvatel ČR mající toto jméno
věk - průměrný věk nositelů jména
pohlaví - zda je jméno mužské či ženské
svátek - datum, kdy má dané jméno svátek
původ - původ jména
Vyřešte následující úkoly.

Vypište na konzoli informace o jménu Jiří.
Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
Vypište na konzoli informace o všech nejčastějších jménech až po Martina.
Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
Vypište průměrný věk a původ pro všechna jména od Libora dolů.
Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce. """

import pandas

jmena = pandas.read_csv("jmena.csv")
jmena = jmena.set_index("jméno")

print(jmena)

# print(jmena.head())
# print(jmena.columns)

# Vypište na konzoli informace o jménu Jiří.
print(jmena.loc["Jiří"])
print(jmena.loc[["Martin","Zuzana","Josef"]])

print(jmena.loc[:"Martin"]) # bez seřazení
print(jmena.sort_values("četnost", ascending=False) [:"Martin"])


print(jmena.loc["Martin":"Tereza", "věk"])
print(jmena.loc["Libor":,["věk", "původ"]])
print(jmena.loc[:,"věk":"původ"])

# ---------------------------------------------------------------------------------------

""" 2
Česká jména
zapni hlavu
Stáhni si soubor jmena.csv se jmény a načti ho tak, aby Pandas vyrobil číselný index. Proveď následující dotazy:

Vypiš všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
Vypiš pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
Vypiš jména a četnost pro jména se slovanským nebo hebrejským původem. Kolik takových jmen je?
Vypiš všechna jména, která mají svátek první 3 dny v prosinci. """

jmena2 = pandas.read_csv("jmena.csv")
print(jmena2)

vek_nad_60 = jmena2[jmena2["věk"] > 60]
print(vek_nad_60)

cetnost_mezi_80_100_tis = jmena2[jmena2["četnost"] >= 80_000 & jmena2["četnost"] <= 100_000]
print(cetnost_mezi_80_100_tis)
