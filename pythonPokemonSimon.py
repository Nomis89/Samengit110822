import pandas as pd

print("Gotta Catch Them All!!")

pokemondf = pd.read_csv("pokemon.csv")

# print(abc.columns)
# print(abc["Name"])


# search = input("welke pokemon wil je zoeken? ")

# for n in pokemondf['Name']:
#    if search == n:
#       print(f"{search} gevonden")

   
def zoekPokemon(dePokemon):
   for pokemon in pokemondf['Name']:
      if dePokemon == pokemon:
         return True
   return False

zoek = input("Welke pokemon wil je zoeken? ")

if zoekPokemon(zoek):
   print("yes")
else:
   print("No")




