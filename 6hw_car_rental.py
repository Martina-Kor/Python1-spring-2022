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

with open('Python1-spring-2022/auta.txt', encoding='utf-8') as vstup:
  zaznamy = vstup.readlines()
  
print(zaznamy)

radky = [zaznam.strip() for zaznam in zaznamy]
print(radky)

radky = [zaznam.split() for zaznam in zaznamy]
print(radky)

radky_oprava = [[zaznam[0], (float(zaznam[1].replace(",", ".")))] for zaznam in radky]
print(radky_oprava)

""" celkovy_pocet_km = [sum(zaznam[1]) for zaznam in radky_oprava]
print(celkovy_pocet_km)

 """