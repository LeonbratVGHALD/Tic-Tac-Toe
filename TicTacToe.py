import tkinter as tk
from tkinter import messagebox
import random

"""Enkel Tic-Tac-Toe (Kryss og Ruter) implementert med tkinter.

Dette programmet er ment som et pedagogisk eksempel og et lite spill.
Koden kombinerer enkel GUI-bygging med grunnleggende spilllogikk.

Funksjoner:
- 3x3-brett med knapper
- Lokal flerspiller (X og O)
- Enspillermodus mot enkel CPU (blander blokkering og tilfeldig trekk)
- Oppdagelse av seier / uavgjort og utheving av vinnende linje
- Restart og meny

Kjør: python3 TicTacToe.py
"""

BOARD_SIZE = 3  # Dimensjon på brettet (3x3)


class TicTacToeApp:
	"""Hovedklasse for spillet. Inneholder GUI-elementer og spilllogikk.

	Attributter (kort):
	- board: 2D-liste med 'X'/'O'/None
	- buttons: 2D-liste med tkinter Button-objekter
	- current_player: 'X' eller 'O'
	- game_over: bool, True når runden er ferdig
	- vs_cpu: backend-flagg (Tkinter BooleanVar) som sier om CPU spiller
	"""

	def __init__(self, root):
		# Referanse til Tk root-vindu
		self.root = root
		root.title("Tripp-Trapp-Tresko")
		root.resizable(False, False)

		# --- Intern tilstand ---
		# board holder den logiske tilstanden; None for tom, 'X' eller 'O' for fylt
		self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
		# buttons holder tkinter Button-objekter for UI
		self.buttons = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
		# Hvem starter (X starter)
		self.current_player = "X"
		# Flagg som stopper nye trekk når runden er avsluttet
		self.game_over = False
		# Backend-flagg for enspillermodus; settes fra menyvalget
		self.vs_cpu = tk.BooleanVar(value=False)

		# --- UI-rammer ---
		# Vi bruker to hovedrammer: en for meny og en for selve spillet.
		self.menu_frame = tk.Frame(root)
		self.game_frame = tk.Frame(root)

		# Bygg UI-elementer i egne metoder for klarhet
		self.build_menu()
		self.build_game_ui()

		# Vis meny først
		self.show_menu()


	def build_menu(self) -> None:
		"""Oppretter hovedmenyens widgeter.

		Menyen inneholder tre valg: Enspiller (CPU), Flerspiller (lokal), Avslutt.
		"""
		menu_label = tk.Label(self.menu_frame, text="Tripp-Trapp-Tresko", font=(None, 18))
		menu_label.pack(pady=(12, 8))

		# Enspiller: setter backend-flagget for CPU og starter spillet
		btn_single = tk.Button(self.menu_frame, text="Enspiller", width=16, command=self.start_singleplayer)
		btn_single.pack(pady=6)

		# Flerspiller: lokal modus uten CPU
		btn_multi = tk.Button(self.menu_frame, text="Flerspiller", width=16, command=self.start_multiplayer)
		btn_multi.pack(pady=6)

		# Avslutt-knapp
		btn_quit = tk.Button(self.menu_frame, text="Avslutt", width=16, command=self.quit_app)
		btn_quit.pack(pady=6)


	def build_game_ui(self) -> None:
		"""Bygger spill-UI: kontrollfelt øverst og 3x3 knapp-rutenett.

		Kontrollfeltet viser nåværende spiller, valgt modus, en restart-knapp
		og en knapp for å gå tilbake til hovedmenyen.
		"""
		# Kontrollfelt
		ctrl = tk.Frame(self.game_frame)
		ctrl.pack(padx=10, pady=6)

		# Label som viser hvilken spillers tur det er
		self.info_label = tk.Label(ctrl, text=f"Tur: {self.current_player}")
		self.info_label.grid(row=0, column=0, padx=6)

		# Moduslabel viser 'Enspiller' eller 'Flerspiller'
		self.mode_label = tk.Label(ctrl, text="Modus: -")
		self.mode_label.grid(row=0, column=4, padx=6)

		# Start på nytt-knapp: nullstiller brettet
		restart_btn = tk.Button(ctrl, text="Start på nytt", command=self.restart)
		restart_btn.grid(row=0, column=1, padx=6)

		# Tilbake til meny
		back_btn = tk.Button(ctrl, text="Tilbake til meny", command=self.show_menu)
		back_btn.grid(row=0, column=2, padx=6)

		# Brettramme: et rutenett med knapper
		self.board_frame = tk.Frame(self.game_frame)
		self.board_frame.pack(padx=10, pady=10)

		# Opprett hver knapp i rutenettet og bind den til on_click
		for r in range(BOARD_SIZE):
			for c in range(BOARD_SIZE):
				b = tk.Button(self.board_frame, text="", width=6, height=3,
						font=(None, 24), command=lambda rr=r, cc=c: self.on_click(rr, cc))
				b.grid(row=r, column=c, padx=3, pady=3)
				self.buttons[r][c] = b


	def get_empty_cells(self):
		"""Returnerer liste over tomme celler som (r, c)-tupler.

		Brukes av CPU-logikk for å finne tilgjengelige trekk.
		"""
		empties = []
		for r in range(BOARD_SIZE):
			for c in range(BOARD_SIZE):
				if self.board[r][c] is None:
					empties.append((r, c))
		return empties


	def find_winning_move(self, player):
		"""Sjekker om `player` har et trekk som vinner umiddelbart.

		Sjekker rader, kolonner og diagonaler. Returnerer (r, c) ved funn,
		ellers None.
		"""
		# Sjekk rader
		for r in range(BOARD_SIZE):
			row = self.board[r]
			if row.count(player) == BOARD_SIZE - 1 and row.count(None) == 1:
				c = row.index(None)
				return (r, c)
		# Sjekk kolonner
		for c in range(BOARD_SIZE):
			col = [self.board[r][c] for r in range(BOARD_SIZE)]
			if col.count(player) == BOARD_SIZE - 1 and col.count(None) == 1:
				r = col.index(None)
				return (r, c)
		# Sjekk diagonaler
		diag1 = [self.board[i][i] for i in range(BOARD_SIZE)]
		if diag1.count(player) == BOARD_SIZE - 1 and diag1.count(None) == 1:
			i = diag1.index(None)
			return (i, i)
		diag2 = [self.board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)]
		if diag2.count(player) == BOARD_SIZE - 1 and diag2.count(None) == 1:
			i = diag2.index(None)
			return (i, BOARD_SIZE - 1 - i)
		return None


	def on_click(self, r, c):
		"""Håndterer spillerens klikk på rute (r, c).

		- Ignorer trekk hvis spillet er over eller ruten er opptatt.
		- Oppdater brett og GUI for spillerens trekk.
		- Sjekk for seier eller uavgjort.
		- Hvis i enspiller-modus, kall CPU for neste trekk.
		"""
		# Ignorer hvis runden er ferdig
		if self.game_over:
			return
		# Ignorer hvis ruten allerede er brukt
		if self.board[r][c] is not None:
			return

		# Oppdater intern modell og knapp
		self.set_cell(r, c, self.current_player)

		# Sjekk om dette var vinnende trekk
		winner, line = self.check_winner()
		if winner:
			self.end_game(winner, line)
			return

		# Sjekk uavgjort
		if self.is_board_full():
			self.end_game(None, None)  # uavgjort
			return

		# Bytt spiller og oppdater info-label
		self.current_player = "O" if self.current_player == "X" else "X"
		self.info_label.config(text=f"Tur: {self.current_player}")

		# Hvis enspillermodus og det er CPU sin tur, kjør CPU-trekket
		if self.vs_cpu.get() and self.current_player == "O":
			# Kall cpu_move direkte for øyeblikkelig respons
			self.cpu_move()


	def cpu_move(self):
		"""CPU sin beslutningslogikk.

		Algoritme:
		1) Hvis CPU kan vinne i ett trekk, ta det.
		2) Ellers: tilfeldig velg mellom å blokkere spillerens umiddelbare
		   vinnermulighet eller å ta et tilfeldig tomt felt.
		"""
		# Unngå trekk hvis runden allerede er over
		if self.game_over:
			return

		# Finn tomme ruter
		empties = self.get_empty_cells()
		if not empties:
			return

		# 1) Sjekk om CPU kan vinne umiddelbart
		win_move = self.find_winning_move("O")
		if win_move is not None:
			r, c = win_move
		else:
			# Velg strategi: noen ganger blokkere, noen ganger tilfeldig
			strategy = random.choice(["random", "block"])
			r, c = None, None
			if strategy == "block":
				block_move = self.find_winning_move("X")
				if block_move is not None:
					r, c = block_move
			# Hvis ingen blokk ble funnet eller strategi var tilfeldig: velg tilfeldig
			if r is None:
				r, c = random.choice(empties)

		# Gjør CPU sitt trekk
		self.set_cell(r, c, "O")

		# Sjekk om CPU vant eller om det ble uavgjort
		winner, line = self.check_winner()
		if winner:
			self.end_game(winner, line)
			return

		if self.is_board_full():
			self.end_game(None, None)
			return

		# Bytt tilbake til menneskelig spiller
		self.current_player = "X"
		self.info_label.config(text=f"Tur: {self.current_player}")


	def set_cell(self, r, c, val):
		"""Oppdaterer den interne brettmodellen og GUI-knappen for (r, c).

		Setter teksten på knappen og deaktiverer den slik at den ikke kan
		brukes igjen i samme runde.
		"""
		self.board[r][c] = val
		self.buttons[r][c].config(text=val, state=tk.DISABLED,
						  disabledforeground="black")


	def check_winner(self):
		"""Sjekker om noen har vunnet.

		Returnerer (vinner_symbol, vinnende_linje) eller (None, None).
		Vinnende_linje er en liste av (r, c)-koordinater som viser hvor linjen er.
		"""
		# Sjekk rader
		for r in range(BOARD_SIZE):
			line = [(r, c) for c in range(BOARD_SIZE)]
			vals = [self.board[r][c] for c in range(BOARD_SIZE)]
			if vals.count(vals[0]) == BOARD_SIZE and vals[0] is not None:
				return vals[0], line

		# Sjekk kolonner
		for c in range(BOARD_SIZE):
			line = [(r, c) for r in range(BOARD_SIZE)]
			vals = [self.board[r][c] for r in range(BOARD_SIZE)]
			if vals.count(vals[0]) == BOARD_SIZE and vals[0] is not None:
				return vals[0], line

		# Sjekk diagonaler
		line = [(i, i) for i in range(BOARD_SIZE)]
		vals = [self.board[i][i] for i in range(BOARD_SIZE)]
		if vals.count(vals[0]) == BOARD_SIZE and vals[0] is not None:
			return vals[0], line

		line = [(i, BOARD_SIZE - 1 - i) for i in range(BOARD_SIZE)]
		vals = [self.board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)]
		if vals.count(vals[0]) == BOARD_SIZE and vals[0] is not None:
			return vals[0], line

		return None, None


	def is_board_full(self):
		"""Returnerer True hvis brettet er fullt (ingen None-verdier)."""
		return all(self.board[r][c] is not None for r in range(BOARD_SIZE) for c in range(BOARD_SIZE))


	def end_game(self, winner, line):
		"""Håndterer avslutning av en runde.

		- Marker vinnerlinjen grafisk
		- Oppdater info-label
		- Vis dialog som spør om spiller ønsker å spille igjen eller gå til meny
		"""
		self.game_over = True
		if winner:
			# Uthev vinnende linje visuelt
			for (r, c) in line:
				self.buttons[r][c].config(bg="#8EF58E")
			# Oppdater informasjonstekst
			self.info_label.config(text=f"{winner} vant!")
			# Force redraw slik at siste trekk og fargeendring vises før dialog
			try:
				self.root.update_idletasks()
			except Exception:
				pass
			# Spør om spiller vil spille igjen
			res = messagebox.askyesno("Spillet er slutt", f"{winner} vant!\nSpille igjen?")
			if res:
				self.restart()
			else:
				self.show_menu()
		else:
			# Uavgjort-case: oppdater label og spør om replay
			self.info_label.config(text="Uavgjort")
			try:
				self.root.update_idletasks()
			except Exception:
				pass
			res = messagebox.askyesno("Spillet er slutt", "Uavgjort\nSpille igjen?")
			if res:
				self.restart()
			else:
				self.show_menu()


	def restart(self):
		"""Starter runden på nytt.

		Resetter den interne brettmodellen og GUI-knappene.
		"""
		self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
		self.game_over = False
		self.current_player = "X"
		# Oppdater label til å vise hvem som starter
		self.info_label.config(text=f"Tur: {self.current_player}")
		# Nullstill alle knapper visuelt
		for r in range(BOARD_SIZE):
			for c in range(BOARD_SIZE):
				b = self.buttons[r][c]
				b.config(text="", state=tk.NORMAL, bg=b.master.cget('bg'))


	def show_menu(self):
		"""Viser hovedmenyen. Skjuler spill-rammen.

		Vi kaller restart for å være sikker på at neste runde starter ren.
		"""
		self.game_frame.pack_forget()
		try:
			self.restart()
		except Exception:
			pass
		self.menu_frame.pack(padx=20, pady=20)


	def show_game(self):
		"""Viser spill-rammen og skjuler meny."""
		self.menu_frame.pack_forget()
		self.game_frame.pack()


	def start_singleplayer(self):
		"""Starter en spillrunde i enspillermodus (CPU spiller som 'O')."""
		self.vs_cpu.set(True)
		self.mode_label.config(text="Modus: Enspiller")
		self.restart()
		self.show_game()


	def start_multiplayer(self):
		"""Starter en spillrunde i lokal flerspillermodus."""
		self.vs_cpu.set(False)
		self.mode_label.config(text="Modus: Flerspiller")
		self.restart()
		self.show_game()


	def quit_app(self):
		"""Avslutter applikasjonen."""
		self.root.destroy()


if __name__ == '__main__':
	root = tk.Tk()
	app = TicTacToeApp(root)
	root.mainloop()

