import pandas

staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

""" print(staty.head())

print(staty.columns)

print(staty.loc["Afghanistan"])
print(staty.loc["Afghanistan":"Algeria"])

# rozdíl pro iloc - poslední hodnota se nevypíše, v loc ano!
print(staty.iloc[0:3])

print(staty.loc[["Afghanistan", "Algeria"], "capital"]) """

# VÝBĚR SLOUPCŮ Z TABULKY
""" print(staty.iloc[:, [1,3]])

print(staty.loc[:, ["alpha3Code", "region"]])

print(staty[["alpha3Code", "region"]])
 """

""" print(staty["area"])
print(staty["area"] < 1000) # vypíše jen true a false podle toho, jestli splňují podmínku

print(staty[staty["area"] < 1000])
male_staty = staty[staty["area"] < 1000]
print(male_staty.info())


lidnate_staty = staty[staty["population"] > 100_000_000]
print(lidnate_staty)

print(staty.sort_values("population", ascending=False) [:10])
print(staty.sort_values("population", ascending=False) [:10]["capital"]) """

male_staty = staty[staty["area"] < 10_000]
lidnate_staty = staty[staty["population"] > 1_000_000]

# chyba v zavorkach 
# print(staty[(staty["area"] < 10_000) & staty["population"] > 1_000_000]))

dotaz_na_male_staty = staty["area"] < 10_000
dotaz_na_lidnate_staty = staty["population"] > 1_000_000
dotaz_na_staty_asie = staty["region"] == "Asia"
dotaz_na_staty_afriky = staty["region"] == "Africa"

dotaz_na_staty_afriky_asie = staty["region"].isin(["Asia", "Africa"])

print(staty[dotaz_na_male_staty & dotaz_na_lidnate_staty])


# 1. zpusob
print(staty[dotaz_na_staty_asie | dotaz_na_staty_afriky])
# 2. zpusob
print(staty[dotaz_na_staty_afriky_asie])

# hází chybu... 
# print(staty["name"])
# print(staty[staty["name"].str.startswith("A")])


print(staty["population"].max())
print(staty["population"].min())
print(staty["population"].sum())
print(staty["population"].mean())