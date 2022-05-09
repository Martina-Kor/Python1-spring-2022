import pandas
import matplotlib

# https://pandas.pydata.org/docs/

# metoda csv
nakupy = pandas.read_csv("nakupy.csv") #máme ve stejné složce, není cesta
print(nakupy)

print(nakupy.info())

info = nakupy.info()
print(info)

# atribut shape, nejprve se vypisují řádky
print(nakupy.shape)

print(nakupy.columns)

# typ série, jeden řádek tabulky
print(nakupy.iloc[1]) # čti aj lok

# můžeme se dívat i na rozsahy
print(nakupy.iloc[5:8]) # od: do + 1
print(nakupy.iloc[8:]) # až do konce
print(nakupy.iloc[:5]) # od začátku
print(nakupy.iloc[-1]) # poslední záznam

print(nakupy.iloc[5, 1])
# print(nakupy.iloc[:5, [0, 3]])
print(nakupy.iloc[[0, 1], [0, 3]])

print(nakupy.iloc[:, 2])
print(nakupy.iloc[0:11, 2])

print(nakupy.head()) # prvních pět řádků tabulky
print(nakupy.tail()) # posledních pět řádků tabulky
