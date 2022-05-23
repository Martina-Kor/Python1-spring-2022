import pandas

jobs = pandas.read_csv(filepath_or_buffer="DataAnalyst.csv")
print(jobs)

# info o proměnných
print(jobs.columns)
print(jobs.head(1))

for col in jobs.columns:
  print(col)

# kolik má soubor řádek
print(jobs.shape) # řádky a sloupce
print(jobs.shape[1]) # vypíše jen počet řádek

# info o pracovní pozici na desátém řádku

print(jobs.iloc[9])

# kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici
print(jobs.iloc[11:20, 1:7]) # u rozsahu se hranaté závorky nepoužívají
# print(jobs.iloc[11:19, [1, 7]]) # když nejsou sloupce vedle sebe

# jen místo výkonu práce
print(jobs.iloc[11:20, 6])

# sloupec podle názvu 
# print(jobs[Job Title]) doplnit jednoduché závorky kolem job title