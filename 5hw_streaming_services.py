
""" 
ukol-05: Streamovací služba
Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa. Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry. Dále chce u filmů evidovat délku a u seriálů počet episod a délku jedné episody.

Vytvoř program, který bude obsahovat tři třídy - Polozka, Film a Serial.
Třída Polozka bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr. Oba atributy nastav ve funkci __init__ a získej je jako parametry.
Třída Film bude potomkem třídy Polozka. Film má kromě názvu a žánru atribut délka.
Třída Serial bude potomkem třídy Polozka. Má kromě názvu a žánru atributy počet epizod a délka epizody.
Všem třídám přidej funkci get_info, která vypíše informace o položce, resp. o filmu a seriálu. Funkce u třídy Polozka vypíše název a žánr. Následně tuto funkci využij ve funkcích u tříd Film a Serial a přidej k ní informaci o délce, resp. počtu episod.
Po naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál a ověř, že vše funguje.

Bonus:
Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají. Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani, který udává celkovou délku pořadů, které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.

Třídám Serial a Film přidej funkci get_celkova_delka, která vrátí celkovou délku filmu/seriálu (u seriálu je to počet episod násobený délkou jedné episody).

Třídě Uzivatel přidej funkci pripocti_zhlednuti, která bude mít jeden parametr. Funkce zvýší atribut udávající celkovou délku sledávní o zadaný parametr.

Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování, využij k tomu funkci get_celkova_delka u objektu a seriálu, abys zjistil(a), kolik minut (nebo hodin) videa celkem uživatel zhlédl.

Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a tuto pomocnou proměnnou potom předáš jako parametr funkci pripocti_zhlednuti. """

class Polozka():
    def __init__(self, jmeno, zanr):
        self.jmeno = jmeno
        self.zanr = zanr
    
    def get_info(self):
        return f'Název: {self.jmeno}, Žánr: {self.zanr}. '

    def get_celkova_delka(self):
        return 0

class Film(Polozka):
    def __init__(self, jmeno, zanr, delka):
        super().__init__(jmeno, zanr)
        self.delka = delka
    
    def get_info(self):
        return super().get_info() + f'Délka filmu je {self.delka} minut.' 
    
    def get_celkova_delka(self):
        return self.delka

class Serial(Polozka):
    def __init__(self, jmeno, zanr, pocet_epizod, delka_epozidy):
        super().__init__(jmeno, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epozidy
    
    def get_info(self):
        return super().get_info() + f'Počet epizod seriálu je {self.pocet_epizod} a délka jedné epizody je {self.delka_epizody} minut.'
    
    def get_celkova_delka(self):
        return self.pocet_epizod * self.delka_epizody


class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0
        
    def watch(self, porad: Polozka):
        self.delka_sledovani += porad.get_celkova_delka()
        return self.delka_sledovani
        
    def get_info(self):
        return f'Uživatel {self.uzivatelske_jmeno} strávil sledováním pořadu {self.delka_sledovani} minut.'


matrix = Film('Matrix', 'scifi', 131)
pulp_fiction = Film('Pulp Fiction', 'drama', 154)
pride_prejudice = Film('Pride & Prejudice', 'romantický', 127)

tbbt = Serial('Teorie velkého třesku', 'komedie', 24, 20)
friends = Serial('Přátelé', 'komedie', 24, 22)
dr_house = Serial('Dr. House', 'drama / mysteriózní', 24, 60)


jan = Uzivatel('Jan Nechvátal')
martina = Uzivatel('Martina Korandová')

jan.watch(matrix)
jan.watch(pulp_fiction)
jan.watch(pride_prejudice)
jan.watch(tbbt)



martina.watch(pride_prejudice)
martina.watch(tbbt)
martina.watch(friends)
martina.watch(dr_house)

print(matrix.get_info())
print(pulp_fiction.get_info())
print(pride_prejudice.get_info())
print(tbbt.get_info())
print(friends.get_info())
print(dr_house.get_info())
print(jan.get_info())
print(martina.get_info())
