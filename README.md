Rask start

Dette repositoriet inneholder en liten Flask-utviklingsserver som server en enkel én-sides Tic-Tac-Toe webapp. Spilllogikken (inkludert CPU-motstanderen) kjøres i nettleseren (klient-side JavaScript) i `static/app.js`, og UI-en bruker et mørkt tema med en egendefinert modal.

1. Opprett og aktiver et virtuelt miljø (anbefalt):

```bash
cd TicTacToe-webapp
python3 -m venv .venv
source .venv/bin/activate
```

2. Installer avhengigheter

Det anbefales å installere avhengigheter i det aktive virtuelle miljøet. Du kan enten
installere fra `requirements.txt` manuelt, eller la skriptet forsøke å installere
`Flask` automatisk for deg — men kun hvis du har aktivert prosjektets virtuelle miljø
(se trinn 1).
Manuell installasjon (anbefalt):
```bash
pip install -r requirements.txt
```

Automatisk (praktisk):

Når du kjører `python TicTacToe.py` med prosjektets venv aktivt (for eksempel etter
og forsøke å installere det med `pip` hvis det mangler. Dersom venv ikke er aktivt,
vil skriptet ikke forsøke installasjon automatisk og vil i stedet vise instruksjoner.


3. Start utviklingsserveren:

```bash
python TicTacToe.py
```

Åpne deretter http://127.0.0.1:5000 i nettleseren din. Sidetittelen viser "Tripp-Trapp-Tresko".

Notater
- UI, CPU-logikk og spillets tilstand er implementert klient-side i `static/app.js`, så serveren fungerer kun som en statisk fil-server.
- For produksjon bør du kjøre appen med en WSGI-server (for eksempel `gunicorn`) i stedet for Flask sin innebygde utviklingsserver.

Feilsøking
-----------

- Port i bruk: Hvis `python TicTacToe.py` feiler fordi port 5000 allerede er i bruk, stopp prosessen som holder porten eller kjør serveren på en annen port:

```bash
python TicTacToe.py --port 5001
# eller
HOST=127.0.0.1 PORT=5001 python TicTacToe.py
```

- Manglende avhengigheter / ModuleNotFoundError: Hvis du får en importfeil for `flask` eller
andre moduler, sørg for at det virtuelle miljøet er aktivt (`source .venv/bin/activate`).

	- Hvis venv er aktivt og `Flask` mangler, kan du enten kjøre:

		```bash
		pip install -r requirements.txt
		```

	- Eller kjøre serveren direkte; når venv er aktiv, vil `python TicTacToe.py` forsøke
		å installere `Flask` automatisk for deg hvis det ikke allerede er installert.

	- Hvis venv ikke er aktivt, vil skriptet vise en kort veiledning om hvordan du oppretter
		og aktiverer et prosjekt-venv i stedet for å endre systemet ditt automatisk.

- 403 / Forbidden i nettleseren: Hvis du tidligere så en 403-feil på `http://127.0.0.1:5000/`, kontroller at Flask-serveren kjører og at du åpner riktig adresse (127.0.0.1:5000). Hvis en annen tjeneste, nettleserutvidelse eller proxy returnerer 403, prøv en annen nettleser eller deaktiver utvidelsen midlertidig.

- Statisk fil lastes ikke (CSS, JS): Kontroller at filen ligger i `static/`-mappen og at `TicTacToe.py` bruker `static_folder='static'`. Sjekk nettleserens konsoll og nettverksfanen for 404-feil og filstier.

-- macOS: Dock-ikoner for GUI-applikasjoner: Å sette et vindusikon via nettleserens favicon endrer ikke Dock-ikonet for Python GUI-applikasjoner.

Hvis du får en konkret feilmelding, lim inn terminalutdataene her så hjelper jeg deg videre.

## Lisens

Dette prosjektet er lisensiert under MIT-lisensen. Se filen `LICENSE` i prosjektets rot for hele lisens-teksten.

Copyright (c) 2025 Leon Kristoffer Bråthen

