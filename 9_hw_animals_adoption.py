""" ukol-09: Adopce zvířat
Stáhni si dataset, který obsahuje seznam zvířat k adopci v ZOO Praha. Zdroj dat je Národní katalog otevřených dat.

Data si načti pomocí metody pandas.read_csv(). Pozor, nastav oddělovač na znak středníku. Využij parametr sep.

Seznam se s daty. Kolik má tabulka řádek a sloupců? Jak se sloupce jmenují?

Které zvíře se nachází na záznamu s indexem 34? Vypiš pomocí iloc název tohoto zvířete v češtině i angličtině.
"""

import pandas

zvirata = pandas.read_csv('Python1-spring-2022/adopce_zvirat.txt', sep=';')

print(zvirata)
print(zvirata.columns)
print(zvirata.iloc[34,1:3])

"""
Bonus
V lekci jsme zmínili, že existují i jiné typy indexů, než jen číselný, který sám vyrobí pandas. Například v kontextu souboru se zvířaty se nabízí hned několik sloupců, které bychom mohli využít jako index, které nejsou číselné.

Načti znovu data, ale tentokrát nastav parametr index_col na název sloupce, který obsahuje název zvířete v češtině. Všimni si, že sloupec teď povýší na index a už se nenachází mezi "běžnými" sloupci.

Pomocí <tvoje-promenna>.index.is_unique ověř, zda je nový index unikátní.

Seřazený index je efektivnější a přehlednější. Seřaď index pomocí metody .sort_index(). Bacha, metoda vrátí novou tabulku se seřazeným indexem. Budeš tedy chtít přepsat původní tabulku.

Vyhledej řádek indexovaný názvem "Outloň váhavý". Namísto metody .iloc využij .loc.

Rozsahy fungují podobně jako u číselných indexů. Vyhledej záznamy mezi "Želva Smithova" a "Želva žlutočelá".

Opakování
Opakování neodevzdávej jako úkol. Místo toho si můžeš své řešení zkontrolovat zde. V případě dotazů nebo alternativního řešení se můžeš obrátit na svého kouče nebo koučku na Slacku.

opery = [
    "Figarova svatba", 
    "Don Giovanni", 
    "La Traviata",
    "Kouzelná flétna"
]
Pomocí chroustání seznamů (list comprehension)
Vytvoř seznam, který obsahuje počet znaků (včetně mezer) každého názvu opery.
Vytvoř seznam, který obsahuje počet slov (ta jsou oddělená mezerami) každého názvu opery.
autori = [
    "Mozart", 
    "Mozart", 
    "Verdi",
    "Mozart"
]
Přibyl nám seznam autorů oper. Jejich pozice odpovídá pozici názvů opery v proměnné opery.

Pomocí chroustání seznamů (list comprehension) vytvoř seznam, který bude obsahovat seznamy o dvou prvcích: [nazev, autor]. Prvek na pozici 0 by tak byl ["Figarova svatba", "Mozart"]

Pomocí chroustání slovníků (dict comprehension) vytvoř slovník, který bude obsahovat název opery jako klíč a autora jako hodnotu. Jeden ze záznamů by tak byl třeba "Kouzelná flétna": "Mozart".

(Vyšší obtížnost) Vytvoř slovník, který bude obsahovat autory oper jako klíče a jejich díla jako hodnoty. Slovník bude mít dva klíče, a jejich hodnota bude vždy seznam řetězců (názvů děl):

{
    "Mozart": ["Figarova svatba", "Don Giovanni", "Kouzelná flétna"], 
    "Verdi": ["La Traviata"]
}
(Vyšší obtížnost) Je možné, že v předchozí úloze bylo potřeba kontrolovat, jestli se ve slovníku klíč už nachází, anebo ne. Abychom se podmínce vyhli, můžeme použít defaultdict z modulu collections. Pomocí dokumentace a příkladu použití zkus upravit předchozí úlohu tak, abychom využili defaultdict. """

""" 
zvirata2 = pandas.read_csv('Python1-spring-2022/adopce_zvirat.txt', sep=';', index_col='nazev_cz')
print(zvirata2)
print(zvirata2.index.is_unique)
zvirata_final = zvirata2.sort_index()
print(zvirata_final)
print(zvirata_final.loc['Outloň váhavý'])
print(zvirata_final.loc['Želva Smithova':'Želva žlutočelá'])  """