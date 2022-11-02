import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import traceback


class ErrorClass(tk.Toplevel):
	def __init__(self, title, message, detail) -> None:
		tk.Toplevel.__init__(self)
		# General App parameters
		self.geometry('350x75')
		self.attributes('-toolwindow', True)
		self.minsize(height=HEIGHT, width=WIDTH)
		self.resizable(width=True, height=False)
		self.details_expanded :bool = False
		self.focus()
		
		# Making the Splashscreen Centered on the Page
		s_width: int = self.winfo_screenwidth()
		s_height: int = self.winfo_screenheight()
		center_x: int = int(s_width / 2 - WIDTH / 2)
		center_y: int = int(s_height / 2 - HEIGHT / 2)
		self.geometry(f'{WIDTH}x{HEIGHT}+{center_x}+{center_y}')



class App(tk.Tk):
	def __init__(self) -> None:
		super(App, self).__init__()
		self.title('Traceback Handling')
		ttk.Style().theme_use('clam')
		self.config(bg='#005680')

		error_button: ttk.Button = ttk.Button(self, text='Click here!', command=self.division_error)
		error_button.pack()

	def division_error(self):
		try:
			1/0
		except Exception as e:
			title : str = 'Error Found!'
			message : str = 'An error {e} has been found!'
			detail: str = traceback.format_exc()
			ErrorClass(title, message, detail)
			App.deiconify(self)


WIDTH : int = 250
HEIGHT : int = 150

if __name__ == "__main__":
	try:
		from ctypes import windll
		windll.shcore.SetProcessDpiAwareness(1)
	except ImportError as e:
		messagebox.showerror(title='Module Not Found', message=f'module {e} not found. Your Program may seem Out of Focus')
	finally:
		app: App = App()
		app.mainloop()
		