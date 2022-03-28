""" 
ukol-04: Evidence aut
Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
4A2 3020	Peugeot 403 Cabrio	47534
1P3 4747	Škoda Octavia	41253
Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

registrační značka automobilu,
značka a typ vozidla,
počet najetých kilometrů,
informaci o tom, jestli je vozidlo aktuálně volné (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).
Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. Poslední atribut nastav jako True, tj. na začátku je vozidlo volné.

Vytvoř objekty, které reprezentují všechny automobily půjčovny.

Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().

Otestuj, že program nedovolí půjčit stejné auto dvakrát.

Bonus:
Přidej třídě Auto metodu vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return. """


class Car:
    def __init__(self,licence_plate, model, km):
        self.licence_plate = licence_plate
        self.model = model
        self.km = km
        self.is_avaliable = True

    def rent(self):
        if self.is_avaliable:
            self.is_avaliable = False
            return "Potvrzuji zapůjčení vozidla."
        else:
            return "Vozidlo není momentálně k dispozici."
    
    def return_car(self, km_new, rental_period):
        self.is_avaliable = True
        self.km = km_new
        if rental_period < 7:
            price = 400 * rental_period   
        else:
            price = 300 * rental_period
        return f'Cena za zapůjčení vozidla je {price} Kč.'

    def get_info(self):
        return f'Zapůjčované auto: {self.licence_plate} –⁠ {self.model} –⁠ {self.km} km'
    
    def __str__(self):
        return self.get_info()
  
peugeot = Car('4A2 3020','Peugeot 403 Cabrio', 47534)
oktavka = Car('1P3 4747', 'Škoda Octavia', 41253)

while True:
    user_choice = input('O zapůjčení jaké značky vozu máte zájem? Škoda nebo Peugeot? ')
    if user_choice.lower() == 'škoda' or user_choice.lower() == 'skoda':
        user_choice = oktavka
        break
    elif user_choice.lower() == 'peugeot': 
        user_choice = peugeot
        break
    else:
        print('Takové auto nemáme, vyberte si prosím značku Škoda nebo Peugeot. ')



print(str(user_choice))
print(user_choice.rent())
print(user_choice.return_car(48000,5))
print(user_choice.get_info())
print(user_choice.rent())
print(user_choice.rent())
print(user_choice.return_car(48500,10))
print(user_choice.get_info())

