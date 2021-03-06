""" ukol-06: Půjčovna aut
Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

Napište program, který na výstup vypíše součet všech ujetých kilometrů.

Nápověda 1
s = "Nejradši mám koláče."
print(s.replace("koláče", "svíčkovou"))
Nápověda 2
Krom metod str (převod na řetězec) a int (převod na celé číslo) existuje i metoda float (převod na desetinné číslo).

Bonus:
Upravte váš program tak, aby jméno souboru k otevření zadal uživatel, abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu. Program ověřte tak, že si soubor auta.txt přejmenujete, nebo si vytvořte nový. """


filename = input('Zadejte nazev souboru: ')

with open('Python1-spring-2022/' + filename) as vstup:
    auta = vstup.readlines()
auta = [radek.split() for radek in auta]

km = [float(auto[1].replace(',', '.')) for auto in auta]

celkem_km = sum(km)

print(celkem_km)