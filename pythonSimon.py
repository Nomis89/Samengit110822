"""
def andereFunctie(mijnParam):
    param = mijnParam * mijnParam
    return param


go = andereFunctie(5)
print(andereFunctie(6))
print(go)

print(andereFunctie(7) + andereFunctie(3)) # de aanroep kan vervangen worden door het geen dat wordt geReturnd
print(49 + 9)

1. Procedeureel programmeren
2. Object oriented programmeren
3. Functioneel programmeren / Stateless programmeren

Stream hierbij heb je nog niet alle data tot je beschikking

"""

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    port = "8889", # alleen op macOS
    user = "root",
    password = "root", # in windows password = ""
    database = "voorbeeld100822"
    )

mijnCursor = mydb.cursor()
mijnCursor.execute("SELECT * FROM boot")
boten = mijnCursor.fetchall()

for b in boten:
    print(b[1])

bootnaam = input("Hoe heet je nieuwe boot? ")
sql = "INSERT INTO  boot (kapitein, naam) VALUES(%s, %s)"
val = ("Robinson", bootnaam)
mijnCursor.execute(sql, val)
mydb.commit()
