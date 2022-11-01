import tkinter as tk
from tkinter import messagebox
import traceback

class App(tk.Tk):
	def __init__(self):
		super(App, self).__init__()
		pass


if __name__ == "__main__":
	try:
		from ctypes import windll
		windll.shcore.SetProcessDpiAwareness(1)
	except ImportError as e:
		messagebox.showerror(title='Module Not Found', message=f'module {e} not found. Your Program may seem Out of Focus')
	finally:
		app: App = App()
		app.mainloop()
		