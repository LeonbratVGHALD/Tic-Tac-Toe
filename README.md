# Tic-Tac-Toe
Tic Tac Toe (Tripp-Trapp-Tresko)
Hva programmet gjør
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

