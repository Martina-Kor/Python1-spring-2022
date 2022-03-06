

baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

# print(baliky)

code_of_parcel =input("Zadejte prosím číslo kód svého balíku: ")

# zajišťuji si, že i když bude číslo balíku zadáno s malými písmeny, převede se na velká, jinak by balík # nebyl správně identifikován.

code_of_parcel = code_of_parcel.upper()
# print(code_of_parcel)

if code_of_parcel in baliky:
      print(f"Balík {code_of_parcel} byl předán kurýrovi. ")
else:
      print(f"Balík {code_of_parcel} zatím nebyl předán kurýrovi.")

