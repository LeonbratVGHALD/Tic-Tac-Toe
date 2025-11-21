# Tic-Tac-Toe (Tripp-Trapp-Tresko)

Et enkelt Tic-Tac-Toe-spill skrevet i Python med et grafisk brukergrensesnitt laget med `tkinter`.

## Innhold
- **Funksjoner:** Spill i én- eller to-spiller modus, enkel CPU, GUI med meny og restart.
- **Krav:** Python 3 med `tkinter` (vanligvis forhåndsinstallert).
- **Kjøring:** Hvordan starte spillet lokalt.

## Funksjoner
- **Enspiller (CPU):** Enkel strategi som kan blokkere og gjøre tilfeldige trekk.
- **Flerspiller:** To spillere på samme maskin.
- **GUI:** 3x3-brett, statusvisning, restart, og tilbake-til-meny.
- **Spilllogikk:** Oppdager seier og uavgjort.

## Krav
- Python 3.x
- `tkinter` (standardmodul i de fleste Python-distribusjoner)

Ingen eksterne Python-pakker kreves.

## Installasjon og kjøring
1. Åpne en terminal i prosjektmappen (der `TicTacToe.py` ligger).
2. Start programmet med:

```
python3 TicTacToe.py
```

På enkelte systemer kan kommandoen være `python TicTacToe.py` avhengig av Python-oppsettet.

## Bruk
- **Velg modus:** Velg "Enspiller" eller "Flerspiller" i hovedmenyen.
- **Gjør trekk:** Klikk på en rute for å plassere `X` eller `O`.
- **Etter runde:** Du blir spurt om du vil spille igjen eller gå tilbake til menyen.

## Hvordan det fungerer (kort)
- Spillbrettet er et 3x3 rutenett av knapper.
- Programmet sjekker vinnende kombinasjoner etter hvert trekk.
- I enspillermodus bruker CPU en enkel strategi: sjekker om den kan vinne, ellers blokkerer eller velger et tilfeldig lovlig trekk.

## Filstruktur
- `TicTacToe.py` — Hovedprogrammet og GUI.
- `README.md` — Denne filen.
- `Documentation/` — Diagrammer og dokumentasjon (f.eks. `Tic Tac Toe Flytskjema.vsdx`).
- `Icon/` — Ikonfiler (PNG/ICO) brukt i prosjektet.

## Videre forbedringer
- Implementere en smartere CPU (f.eks. minimax)
- Forbedre UI-design og tilgjengelighet
- Legge til enkel statistikk (seire/tap)

## Bidra
Ønsker du å forbedre prosjektet: åpne issues eller pull requests og beskriv endringen/feilen.

## Lisens
Ingen eksplisitt lisens er inkludert. Legg gjerne til en `LICENSE`-fil hvis du vil gjøre koden fri å bruke.

## Forfatter
LeonbratVGHALD

---

Takk for at du bruker og tester Tic-Tac-Toe! Gi gjerne beskjed hvis du vil at jeg skal legge til en engelsk versjon eller generere en enkel `requirements.txt`/`LICENSE`.
# Tic-Tac-Toe (Tripp-Trapp-Tresko)

Dette programmet er et digitalt Tic Tac Toe-spill (Tripp-Trapp-Tresko) laget i Python med Tkinter for grafisk grensesnitt.

Funksjoner:

Hovedmeny med valg: Enspiller, Flerspiller, Avslutt.

Enspiller-modus: Spill mot en enkel CPU som kombinerer blokkering og tilfeldige trekk.

Flerspiller-modus: To personer kan spille mot hverandre lokalt.

Spilllogikk: Oppdager vinnende kombinasjoner og uavgjort.

GUI: 3x3 brett med knapper, statusvisning og kontrollknapper.

Restart og menyvalg etter endt runde.


Hvordan det brukes

Start programmet:

Velg modus i hovedmenyen:

Enspiller: Spill mot CPU.
Flerspiller: Spill mot en annen person.
Avslutt: Lukker programmet.


Spill:

Klikk på en rute for å plassere din brikke (X eller O).
Programmet viser turstatus og oppdaterer brettet.


Etter en runde:

Dialog spør om du vil spille igjen eller gå tilbake til menyen.




Installationskrav

Python 3.x
Biblioteker:

tkinter (standard i Python)
random (standard)


Ingen eksterne pakker kreves.


Endringer fra planlagt løsning

Planlagt: CPU skulle være "ikke smart", kun tilfeldig eller blokkere.
Gjennomført: CPU implementert med enkel strategi:
Sjekker om den kan vinne i ett trekk.
Ellers velger tilfeldig mellom blokkering og tilfeldig trekk.

Planlagt: Kun grunnleggende GUI.
Gjennomført: GUI med meny, statusfelt, restart-knapp og tilbake-til-meny-knapp.

Planlagt: Kun funksjonell testing.
Gjennomført: Dialogbokser for replay og bedre feilhåndtering.


Forslag til forbedringer / videreutvikling

Smartere CPU: Implementere minimax-algoritme for optimal spillstrategi.
Designforbedringer: Bedre farger, animasjoner og responsivt layout.
Statistikk: Lagre antall seire/tap og vise historikk.
Lyd: Legge til lydeffekter ved trekk og seier.
Mobiltilpasning: Lage en versjon som fungerer på mobil eller som web-app.

