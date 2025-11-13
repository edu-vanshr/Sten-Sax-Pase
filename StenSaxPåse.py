import random as rand  # Enda tillåtna biblioteket

# ------------------------- HUVUDFUNKTION -------------------------

def spela_sten_sax_påse():
    """
    Huvudfunktion som styr spelet.
    Introducerar spelet, frågar namn och antal omgångar.
    Loopar igenom alla omgångar, visar resultat och slutpoäng.
    """
    print("Nu ska vi spela Sten, Sax, Påse!")

    # Yttre loop – så man kan spela flera gånger
    while True:
        # Fråga spelarens namn
        spelare_namn = hälsa_spelare()
        antal_omgångar = fråga_antal_omgångar()

        valmöjligheter = ["sten", "sax", "påse"]
        poäng_spelare = 0
        poäng_dator = 0

        # Spela de valda omgångarna
        for runda in range(1, antal_omgångar + 1):
            print(f"\n--- Omgång {runda} ---")
            vinnare = spela_en_omgång(spelare_namn, valmöjligheter)

            # Uppdatera poäng
            if vinnare == "spelare":
                print(f"{spelare_namn} vinner omgången!")
                poäng_spelare += 1
            elif vinnare == "dator":
                print("Datorn vinner omgången!")
                poäng_dator += 1
            else:
                print("Oavgjort!")

            # Visa aktuell ställning
            print(f"Ställning: {spelare_namn} {poäng_spelare} - Datorn {poäng_dator}")

        # Visa slutresultat
        visa_resultat(spelare_namn, poäng_spelare, poäng_dator)

        # Fråga om spelaren vill spela igen
        if not spela_igen():
            print("\nProgrammet avslutas. Tack för att du spelade!")
            break


# ------------------------- HJÄLPFUNKTIONER -------------------------

def hälsa_spelare():
    """Frågar efter spelarens namn och hälsar."""
    while True:
        namn = input("Ange ditt spelarnamn -> ").strip()
        if namn:
            print(f"Trevligt att träffas {namn}!")
            return namn
        else:
            print("Ogiltigt svar! Namnet får inte vara tomt. Försök igen.")

def fråga_antal_omgångar():
    """Frågar spelaren hur många omgångar de vill spela."""
    while True:
        svar = input("Hur många omgångar vill du spela? -> ").strip()
        if svar.isdigit() and int(svar) > 0:
            return int(svar)
        else:
            print("Ogiltigt svar! Skriv ett positivt heltal, t.ex. 3.")

def spela_en_omgång(spelare_namn, valmöjligheter):
    """Kör en omgång Sten–Sax–Påse."""
    while True:
        spelar_val = input(f"{spelare_namn}, välj mellan Sten, Sax eller Påse -> ").lower()
        if spelar_val in valmöjligheter:
            break
        print("Ogiltigt val! Skriv 'sten', 'sax' eller 'påse'.")

    dator_val = rand.choice(valmöjligheter)

    # Visa bådas val
    print(f"{spelare_namn} valde: {spelar_val}")
    print(f"Datorn valde: {dator_val}")

    # Bestäm vinnare
    if spelar_val == dator_val:
        return "oavgjort"
    elif (spelar_val == "sten" and dator_val == "sax") or \
         (spelar_val == "sax" and dator_val == "påse") or \
         (spelar_val == "påse" and dator_val == "sten"):
        return "spelare"
    else:
        return "dator"

def visa_resultat(spelare_namn, poäng_spelare, poäng_dator):
    """Skriver ut slutresultatet efter alla omgångar."""
    print("\n-------- Slutresultat ---------")
    print(f"{spelare_namn}s poäng: {poäng_spelare}")
    print(f"Datorns poäng: {poäng_dator}")

    if poäng_spelare > poäng_dator:
        print(f"Grattis {spelare_namn}! Du vann spelet!")
    elif poäng_spelare < poäng_dator:
        print("Datorn vann spelet!")
    else:
        print("Spelet slutade oavgjort!")

def spela_igen():
    """Frågar spelaren om hen vill spela igen."""
    while True:
        svar = input("\nVill du spela igen? (ja/nej) -> ").strip().lower()
        if svar in ["ja", "j"]:
            return True
        elif svar in ["nej", "n"]:
            return False
        else:
            print("Ogiltigt svar! Skriv 'ja' eller 'nej'.")


# ------------------------- START -------------------------
spela_sten_sax_påse()


