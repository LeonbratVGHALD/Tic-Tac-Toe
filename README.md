Rask start

Dette repositoriet inneholder en liten Flask-utviklingsserver som server en enkel én-sides Tic-Tac-Toe webapp. Spilllogikken (inkludert CPU-motstanderen) kjøres i nettleseren (klient-side JavaScript) i `static/app.js`, og UI-en bruker et mørkt tema med en egendefinert modal.

1. Opprett og aktiver et virtuelt miljø (anbefalt):

```bash
cd TicTacToe-webapp
python3 -m venv .venv
source .venv/bin/activate
```

2. Installer avhengigheter:

```bash
pip install -r requirements.txt
```

3. (Valgfritt) Legg til en favicon: kopier en PNG-ikonfil inn i `static/`-mappen og kall den `favicon.png`.
Fra prosjektets rot kan du for eksempel kopiere et eksisterende ikon slik:

```bash
cp ../Icon/PNG/16_128.png static/favicon.png
```

4. Start utviklingsserveren:

```bash
python TicTacToe.py
```

Åpne deretter http://127.0.0.1:5000 i nettleseren din. Sidetittelen viser "Tripp-Trapp-Tresko".

Notater
- UI, CPU-logikk og spillets tilstand er implementert klient-side i `static/app.js`, så serveren fungerer kun som en statisk fil-server.
- Appen bruker en egendefinert, stilbar bekreftelsesmodal og et mørkt tema definert i `static/style.css`.
- For produksjon bør du kjøre appen med en WSGI-server (for eksempel `gunicorn`) i stedet for Flask sin innebygde utviklingsserver.
- Hvis du ønsker at CPU-logikk eller vedvarende lagring skal håndteres server-side (REST API), kan jeg legge til endepunkter for det.

Feilsøking
-----------

- Port i bruk: Hvis `python TicTacToe.py` feiler fordi port 5000 allerede er i bruk, stopp prosessen som holder porten eller kjør serveren på en annen port:

```bash
python TicTacToe.py --port 5001
# eller
HOST=127.0.0.1 PORT=5001 python TicTacToe.py
```

- Manglende avhengigheter / ModuleNotFoundError: Sørg for at det virtuelle miljøet er aktivt (`source .venv/bin/activate`) og at du har kjørt `pip install -r requirements.txt`.

- 403 / Forbidden i nettleseren: Hvis du tidligere så en 403-feil på `http://127.0.0.1:5000/`, kontroller at Flask-serveren kjører og at du åpner riktig adresse (127.0.0.1:5000). Hvis en annen tjeneste, nettleserutvidelse eller proxy returnerer 403, prøv en annen nettleser eller deaktiver utvidelsen midlertidig.

- Statisk fil lastes ikke (favicon, CSS, JS): Kontroller at filen ligger i `static/`-mappen og at `TicTacToe.py` bruker `static_folder='static'`. Sjekk nettleserens konsoll og nettverksfanen for 404-feil og filstier.

- macOS: Dock-ikoner for GUI-applikasjoner: Å sette et vindusikon via nettleserens favicon endrer ikke Dock-ikonet for Python GUI-applikasjoner. For webappen vises favicon i nettleseren; kopier en PNG til `static/favicon.png` for å få et ikon i fanen.

Hvis du får en konkret feilmelding, lim inn terminalutdataene her så hjelper jeg deg videre.
