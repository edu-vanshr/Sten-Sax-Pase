import random as rand
val = ["sten", "sax", "påse"]

while True:

    print("Hej! Jag är datorn i spelet Sten-Sax-Påse.")
spelare_namn = int(input("Låt oss börja med att du anger ditt spelarnamn -> "))
print(f"Trevligt att träffas, {spelare_namn}!\nVi spelar 3 omgångar, lycka till :)")
poäng_spelare = 0
poäng_dator = 0
antal_omgångar = 3
for runda in range(1, antal_omgångar + 1):
    print("--- Omgång {runda} ---")
spelar_val = int(input(f"{spelare_namn}, välj mellan Sten, Sax eller Påse -> ")).lower()
while spelar_val not in val:
    print("Ogiltigt val! Välj mellan Sten, Sax eller Påse -> ").lower()
dator_val = random.choice(val)
print(f"Datorn valde: {dator_val}")