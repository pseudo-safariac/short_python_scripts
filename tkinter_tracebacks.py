import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import traceback

"""The program is built as an example of how tkinter can handle exceptions and how the traceback can be displayed without causing the GUI to exit its mainloop.
	Any exception can then be safely handled and more information can be collected for use especially with Product Designers."""

WIDTH : int = 250
HEIGHT : int = 150

class ErrorClass(tk.Toplevel):
	def __init__(self, title, message, detail) -> None:
		tk.Toplevel.__init__(self)
		# General App parameters
		self.geometry('350x75')
		self.attributes('-toolwindow', True)
		self.minsize(height=HEIGHT, width=WIDTH)
		self.resizable(width=True, height=False)
		self.title(title)
		self.switch :bool = False
		self.rowconfigure(1, weight=0)
		self.columnconfigure(1, weight=1)
		center(self)

		# Add the Button Frame section
		button_frame: ttk.Frame = ttk.Frame(self)
		button_frame.grid(row=0, column=0, sticky='nsew')
		button_frame.rowconfigure(1, weight=0)
		button_frame.columnconfigure(1, weight=1)

		# Add widgets to the Button Frame
		message_label: ttk.Label = ttk.Label(button_frame, text=message)
		message_label.grid(row=0, column=0, padx=(7,7), pady=(7,7))

		close_button : ttk.Button = ttk.Button(button_frame, text='Close', command=self.destroy)
		close_button.grid(row=1, column=0, sticky='e')

		details_button : ttk.Button = ttk.Button(button_frame, text='Details', command=self.more_details)
		details_button.grid(row=1, column=0, sticky='w')
		
		# Add the message Frame section
		message_frame: ttk.Frame = ttk.Frame(self)
		message_frame.grid(row=1, column=0, sticky='nsew', padx=(7,7), pady=(7,7))
		message_frame.rowconfigure(1, weight=0)
		message_frame.columnconfigure(1, weight=1)

		# Add widgets to message frame
		self.main_text: tk.Text = tk.Text(message_frame, height=6)
		self.main_text.insert(1.0, detail)
		self.main_text.config(state='normal')

		self.scrollbar: ttk.Scrollbar = ttk.Scrollbar(message_frame, command=self.main_text.yview)
		self.main_text.config(yscrollcommand=self.scrollbar.set)

	def more_details(self) -> None:
		if self.switch:
			self.main_text.grid_forget()
			self.scrollbar.grid_forget()
			self.geometry('350x75')
			self.switch : bool = False

		else:
			self.main_text.grid(row=0, column=0, sticky='nsew')
			self.scrollbar.grid(row=0, column=1, sticky='nsew')
			self.geometry('350x160')
			self.switch : bool = True


class App(tk.Tk):
	def __init__(self) -> None:
		super(App, self).__init__()
		self.title('Traceback Handling')
		ttk.Style().theme_use('clam')
		self.config(bg='#005680')
		center(self)

		error_button: ttk.Button = ttk.Button(self, text='Click here!', command=self.division_error)
		error_button.pack()

	def division_error(self) -> None:
		try:
			1/0
		except Exception as e:
			title : str = 'Error Found!'
			message : str = 'An error {e} has been found!'
			detail: str = traceback.format_exc()
			ErrorClass(title, message, detail)
			App.deiconify(self)


def center(self):
	# Ensures the Splashscreen is centered on the Screen
		s_width: int = self.winfo_screenwidth()
		s_height: int = self.winfo_screenheight()
		center_x: int = int(s_width / 2 - WIDTH / 2)
		center_y: int = int(s_height / 2 - HEIGHT / 2)
		return self.geometry(f'{WIDTH}x{HEIGHT}+{center_x}+{center_y}')
		

if __name__ == "__main__":
	try:
		from ctypes import windll
		windll.shcore.SetProcessDpiAwareness(1)
	except ImportError as e:
		messagebox.showerror(title='Module Not Found', message=f'module {e} not found. Your Program may seem Out of Focus')
	finally:
		app: App = App()
		app.mainloop()
		
		"""0328 - born on 31/10/2022, male"""