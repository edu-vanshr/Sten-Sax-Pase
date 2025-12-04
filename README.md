# Sten-Sax-Pase

Detta projekt är en enkel implementation av spelet Sten, Sax, Påse där spelaren möter datorn i ett valfritt antal omgångar. Programmet är textbaserat och körs i terminalen.

## Kort beskrivning a programmet

Spelet låter användaren:

- Skriva in sitt namn
- Bestämma antal omgångar
- Spela Sten–Sax–Påse mot datorn
- Se resultat efter varje omgång
- Få ett slutresultat med möjlighet att spela igen
- Datorn gör sina val slumpmässigt.

## Hur programmet startas och körs

1. Navigera till filen StenSaxPåse.py
2. Klicka på "Run" knappen som ligger längst upp till höger
3. Programmet startas då med att fråga dig om din spelarnamn
4. Njuta av spelet!

## Exempel på in- och utmatning

Nu ska vi spela Sten, Sax, Påse!
Ange ditt spelarnamn -> Vansh
Trevligt att träffas Vansh!
Hur många omgångar vill du spela? -> 3

--- Omgång 1 ---
Vansh, välj mellan Sten, Sax eller Påse -> sten
Vansh valde: sten
Datorn valde: sax
Vansh vinner omgången!
Ställning: Vansh 1 - Datorn 0

--- Omgång 2 ---
Vansh, välj mellan Sten, Sax eller Påse -> påse
Vansh valde: påse
Datorn valde: sten
Datorn vinner omgången!
Ställning: Vansh 1 - Datorn 1

--- Omgång 3 ---
Vansh, välj mellan Sten, Sax eller Påse -> sax
Vansh valde: sax
Datorn valde: sax
Oavgjort!
Ställning: Vansh 1 - Datorn 1

-------- Slutresultat ---------
Vanshs poäng: 1
Datorns poäng: 1
Spelet slutade oavgjort!

Vill du spela igen? (ja/nej) -> nej
Programmet avslutas. Tack för att du spelade!

## Loggbok

Datum - 4/11/2025

Vad gjorde vi idag - Vi började projektet med att välja ett enkelt spel: Sten, Sax, Påse, för att snabbt komma igång med programmeringen. Under denna lektion skapade vi programmets grundstruktur. Vi importerade random och byggde huvudfunktionen spela_sten_sax_påse(), som ansvarar för att starta spelet, fråga efter namn, bestämma antal omgångar, köra rundorna och hålla koll på poängen.
Vi planerade spelet genom att dela upp det i flera mindre funktioner, till exempel för att spela en rond, för att fråga antal omgångar och för att hantera spelarens namn. Detta gör koden tydligare och enklare att testa. Vi lade även till listan med valmöjligheter: ["sten", "sax", "påse"], som både spelaren och datorn använder.
Lektionens resultat blev en stabil grund där spelets struktur och huvudlogik är redo. Nästa steg är att skriva funktionen som avgör vinnaren, skapa datorns slumpval och hantera felaktiga inmatningar.

Problem/Frågeställningar som uppstod? - Eftersom spelet består av flera moment — fråga spelarens namn, antal omgångar, spela rundor och uppdatera poäng — behövde vi bestämma hur dessa delar skulle organiseras. Skulle allt ligga i huvudfunktionen eller delas upp?

Lösning - För att bemöta problemet valde vi att dela upp programmet i flera mindre funktioner, istället för att samla all kod i huvudfunktionen.



Datum - 6/11/2025

Vad gjorde vi idag - Under lektionen utvecklade vi spelet genom att:
- Få funktionen spela_en_omgång() att fungera korrekt, så att den jämför spelarens och datorns val och avgör vinnaren.
- Uppdatera poängen automatiskt och visa aktuell ställning efter varje runda.
- Skapa funktionen visa_resultat() för ett tydligt slutresultat.
- Lägga till möjlighet för spelaren att spela igen, med ett avskedsmeddelande om hen väljer nej.

Problem/Frågeställningar som uppstod? - Vi hade inga problem med kodningen, men vi var osäkra på hur git add, git commit och git push fungerade.

Lösning - Vi tog hjälp av vår lärare Nikodemus som förklarade processen och visade hur kommandona används korrekt för framtida lektioner.



Datum - 11/11/2025

Vad vi gjorde idag - Under lektionen arbetade vi med att strukturera spelet bättre genom att skapa små, tydliga funktioner:

- hälsa_spelare() – frågar efter spelarens namn och kontrollerar att det inte är tomt.
- fråga_antal_omgångar() – frågar antal omgångar och säkerställer att svaret är ett positivt heltal.
- spela_en_omgång() – hanterar spelarens val, datorns slumpval och avgör vinnaren.
- visa_resultat() – visar slutpoäng och vem som vann.
- spela_igen() – frågar om spelaren vill fortsätta spela och accepterar både ja/nej och j/n.

Problem/Frågeställningar som uppstod - Programmet hanterade inte felaktiga svar när användaren skrev något annat än ett heltal, t.ex. bokstäver, tomt svar eller extra mellanslag, vilket kunde orsaka fel eller krascher.

Lösning - Vi använde strip() för att ta bort mellanslag, isdigit() för att kontrollera att svaret endast innehåller siffror och int(svar) > 0 för att säkerställa ett giltigt heltal. Detta gör spelet robust mot olika typer av användarinmatning.



Datum - 13/11/2025

Vad vi gjorde idag - Idag färdigställde vi kommentarerna och genomförde en noggrann kodgranskning för att säkerställa att inga fel fanns kvar. Lyckligtvis visade sig koden vara felfri och kunde utan problem pushas till GitHub. Efter den avslutade granskningen klonades projektet från GitHub, och vi förde en diskussion kring kodens struktur och funktionalitet.

Problem/Frågeställningar som uppstod: Inga problem än så länge

Lösning - Inga lösningar krävdes


## Buggar, begränsningar och framtida förbättringar

Buggar:

- Programmet hanterar inte specialtecken eller konstiga inputs i namnet.
- Felhantering är enkel och stoppar inte alla ogiltiga situationer.

Begränsningar:

- Endast en spelare mot datorn.
- Textbaserat, ingen grafisk design.
- Datorns val är helt slumpmässigt — ingen strategi.

Framtida förbättringar:

- Införa en AI-strategi så datorn blir svårare.
- Implementera multiplayer-läge.
- Visa statistik över tidigare matcher.
- Lägga till ljud eller animationer.
