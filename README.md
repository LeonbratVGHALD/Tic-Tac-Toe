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

## Lisens
Dette prosjektet er lisensiert under MIT-lisensen. Se filen `LICENSE` for full lisens-tekst.

Copyright (c) 2025 Leon Kristoffer Bråthen

## Forfatter
Leon Kristoffer Bråthen (GitHub: `LeonbratVGHALD`)