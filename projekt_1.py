"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiří Vitouch
email: jivi@centrum.cz
discord: jirkav._
"""

# Uložená správná jména a hesla
users = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
}

oddelovac = "-" * 40

# Získání uživatelského jména a hesla od uživatele
uzivatel = input("username: ")
heslo = input("password: ")

# Ověření přihlášení uživatele
if uzivatel in users and heslo == users[uzivatel]:
    print(oddelovac)
    print("Welcome to the app,", uzivatel)
    print("We have 3 texts to be analyzed.", oddelovac, sep="\n")
else:
    print("Unregistered user, terminating the program...")
    quit()


# texty
    
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Rozdělení textů do jednotlivých listů
text_1 = [TEXTS[0]]
text_2 = [TEXTS[1]]
text_3 = [TEXTS[2]]

# Výběr mezi 3 texty
vyber_textu = input("Enter a number btw. 1 and 3 to select: ")
if not vyber_textu.isdigit():
    print("It's not a number, terminating the program...")
    quit()
elif int(vyber_textu) != 1 and int(vyber_textu) != 2 and int(vyber_textu) != 3:
    print("It's not a number from range, terminating the program...")
    quit()
else:
    print(oddelovac)

# Práce s textem
if vyber_textu == "1":
    vybrany_text = text_1[0]
elif vyber_textu == "2":
    vybrany_text = text_2[0]
else:
    vybrany_text = text_3[0]

# Rozdělení textu na slova
slova = vybrany_text.split()

# Počet slov ve vybraném textu
pocet_slov = len(slova)
print(f"There are {pocet_slov} words in the selected text.")

# Počet slov s prvním velkým písmenem
prvni_velke = 0
for slovo in slova:
    if slovo.istitle():
        prvni_velke += 1
print(f"There are {prvni_velke} titlecase words.")

# Počet slov CELE VELKÉ
cele_velke = 0
for slovo in slova:
    if slovo.isupper() and slovo.isalpha():
        cele_velke +=1
print(f"There are {cele_velke} uppercase words.")

# Počet slov s malými písmeny
male_slovo = 0
for slovo in slova:
    if slovo.islower():
        male_slovo +=1
print(f"There are {male_slovo} lowercase words.")

# Počet číslic
cislice = 0
for slovo in slova:
    if slovo.isnumeric():
        cislice += 1
print(f"Theer are {cislice} numeric strings.")

# Součet čísel v textu
soucet = 0
for slovo in slova:
    if slovo.isnumeric():
        cislo = int(slovo)
        soucet += cislo
print(f"The sum of all the numbers {soucet}")
print(oddelovac)

# Výpočet délky slov a jejich počet
slova_delka = {}
for slovo in slova:
    delka = len(slovo)
    if delka in slova_delka:
        slova_delka[delka] += 1
    else:
        slova_delka[delka] = 1

# Vytvoření tabulky
print("LEN| OCCURENCES |NR.")
print(oddelovac)
for delka, pocet in sorted(slova_delka.items()):
    stars = "*" * pocet
    print(f"{delka:3}|{stars:<12}|{pocet:2}")







    



 
