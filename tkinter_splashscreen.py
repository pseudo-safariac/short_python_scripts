#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
from tkinter.messagebox import showinfo

import threading
import time

class SplashScreen(tk.Tk):
	"""This class hold the Widgets that get painted when the app launches. 
	It's main purpose is to simulate an app launch delay."""
	def __init__(self) -> None:
		super(SplashScreen,self).__init__()
		self.attributes('-topmost', 1)
		self.attributes('-alpha', 0.0)
		self.overrideredirect(True)
		self.config(bg=COLORS['Dark blue'])

		# Visual Fade-in effect
		center(self)
		visual_fade: threading.Thread = threading.Thread(target=self.alpha_settings)
		visual_fade.start()

		# Styling of the widgets
		s: ttk.Style = ttk.Style()
		s.theme_use('clam')
		s.configure('TButton', background = [('focus', COLORS['Dark blue'])], foreground = [('focus', COLORS['Dark blue'])])

		# Styling Company Label Widget
		s.configure('company.TButton', background=COLORS['Dark blue'], foreground= COLORS['Light blue_2'], font= ('Helvetica', 49, 'bold'), borderwidth= 0, width=11)
		s.map('company.TButton', background=[('active', COLORS['Dark blue'])], foreground=[('active', COLORS['Light white'])])

		# Styling Lab Label Widget
		s.configure('lab.TButton', background= COLORS['Dark blue'],foreground= COLORS['Light blue_2'], font=('Proxima Nova', 27, 'bold', 'italic'), borderwidth=0, width=4)
		s.map('lab.TButton', background=[('active', COLORS['Dark blue'])],foreground=[('active', COLORS['Light white'])])

		# Styling close Label Widget
		s.configure('close.TButton', background=COLORS['Dark blue'],foreground=COLORS['Light white'], font=('Proxima Nova', 9, 'bold'), borderwidth=0, width=6)
		s.map('close.TButton', background=[('active', COLORS['other'])], foreground=[('active', COLORS['Light white'])])

		# Adding Button Widgets
		company_label: ttk.Button = ttk.Button(self, text = 'WALTER\'S', style= 'company.TButton', command=self.destroy)
		company_label.place(x=50, y=80)

		lab_label: ttk.Button = ttk.Button(self, text='Lab', style= 'lab.TButton', command=self.destroy)
		lab_label.place(x=440, y=180)

		close_button : ttk.Button = ttk.Button(self, text='close', style= 'close.TButton', command= self.destroy)
		close_button.place(x=570, y=0)

	def alpha_settings(self) -> None:
		"""The function gradually changes the contrast of the tkinter application."""
		timer : int | float = 50
		contrast : float | int = 0.5
		while timer != 0:
			self.attributes('-alpha', contrast)
			contrast += 0.01
			timer -= 1
			time.sleep(0.03)


class Login(tk.Tk):
	"""
	The class will act as the login page of the GUI. 

	It creates the login environment, enhances it with some basic UI information to assist the user with the login.
	"""
	def __init__(self) -> None:
		super(Login, self).__init__()
		self.wm_title('Splash Login')
		self.attributes('-topmost', 1)
		self.attributes('-alpha', 0.99)
		self.wm_overrideredirect(True)
		self.config(bg=COLORS['Dark blue'])
		center(self)

		self.create_widgets()
	def create_widgets(self) -> None:
		"""
		Creates and places the widgets to be used in the window and styles them for a better UI experience.
		"""
		# Styling
		s : ttk.Style = ttk.Style()
		s.theme_use('clam')

		# Styling Clean Water Button Widget
		s.configure('clean_water.TButton', background=COLORS['Dark blue'], foreground=COLORS['Light blue_2'], font=('Helvetica', 29, 'bold'), borderwidth=0)
		s.map('clean_water.TButton', background=[('active', COLORS['Dark blue'])], lightcolor=[('focus', COLORS['new_2'])], foreground=[('active', COLORS['Light white'])])
		
		# Styling Section Button Widget
		s.configure('section_button.TButton', foreground=COLORS['Grey'],background=COLORS['Dark blue'], borderwidth=0, font=('Proxima Nova', 14, 'bold', 'italic'))
		s.map('section_button.TButton', background=[('active', COLORS['Dark blue'])],foreground=[('active', COLORS['Light white'])], alternate= [('active', 'white')])
		
		# Styling Username Label Widget
		s.configure('username.TLabel', font=('Arial', 14, 'bold'),background='#231651', foreground=COLORS['Light white'], borderwidth=0)
		s.map('username.TLabel', background=[('active', COLORS['Dark blue'])],foreground=[('active', COLORS['Light blue_2'])])
		
		# Styling Password Label Widget
		s.configure('password.TLabel', font=('Arial', 14, 'bold'),background=COLORS['Dark blue'], foreground=COLORS['Light white'], borderwidth=0)
		s.map('password.TLabel', background=[('active', COLORS['Dark blue'])],foreground=[('active', COLORS['Light blue_2'])])
		
		# Styling Login Button Widget
		s.configure('login.TButton', font=('Helvetica', 12, 'bold'),background=COLORS['Dark blue'], foreground=COLORS['Grey'],borderwidth=0)
		s.map('login.TButton', background=[('active', COLORS['other'])],foreground=[('active', COLORS['Light white'])])

		# Styling Forgot password Button Widget
		forgot_pass_font: Font = Font(family='Times', size=9, underline=True, weight='bold')
		s.configure('forgot_pass.TButton', font=forgot_pass_font, background=COLORS['Dark blue'], foreground= COLORS['Grey'], borderwidth=0)
		s.map('forgot_pass.TButton', background=[('active', COLORS['Dark blue'])], foreground=[('active', COLORS['Light white'])])

		# Styling close Button Widget
		s.configure('close.TButton', font=('Helvetica', 9, 'bold'),background=COLORS['Dark blue'], foreground=COLORS['Grey'],borderwidth=0)
		s.map('close.TButton', background=[('active', COLORS['other'])],foreground=[('active', COLORS['Light white'])])

		# Adding Widgets
		clean_water: ttk.Button = ttk.Button(self, text='CLEAN WATER', style= 'clean_water.TButton')
		clean_water.place(x=50, y=0)

		section_button: ttk.Button = ttk.Button(self, text='Section', style='section_button.TButton')
		section_button.place(x=380, y=60)

		self.username_text: ttk.Label = ttk.Label(self, text='Username :', style='username.TLabel')
		self.username_text.place(x=90, y=120)

		self.password_text: ttk.Label = ttk.Label(self, text='Password :', style='password.TLabel')
		self.password_text.place(x=90, y=190)

		login_button: ttk.Button = ttk.Button(self, text='Login', style= 'login.TButton')
		login_button.place(x= 450, y= 260)

		forgot_password: ttk.Button = ttk.Button(self, text='Forgot Password',style='forgot_pass.TButton', command=self.forgot_password_messagebox)
		forgot_password.place(x=100, y=260)

		close_button: ttk.Button = ttk.Button(self, text='close', style='close.TButton', command=self.destroy)
		close_button.place(x=540, y=0)
		
		self.notification_message: ttk.Label = ttk.Label(self, background=COLORS['Dark blue'], font=('Helvetica', 14))
		self.notification_message.place(x=200, y=85)
		
		# Binding keyboard input
		self.bind('<Return>', self.confirm_signin)

		# Adding Entries
		self.username_entry_var: tk.StringVar = tk.StringVar()
		self.password_entry_var: tk.StringVar = tk.StringVar()

		username_entry: ttk.Entry = ttk.Entry(self, font=('Arial', 14, 'bold'),cursor= 'xterm', textvariable=self.username_entry_var, takefocus=True)
		username_entry.focus()
		username_entry.place(x=260, y=120)

		password_entry: ttk.Entry = ttk.Entry(self,font=('Arial', 14, 'bold'),cursor='xterm', show='*', textvariable= self.password_entry_var)
		password_entry.place(x=260, y=190)
	
	def confirm_signin(self, event) -> None:
		if self.username_entry_var.get() == "Admin":
			print(f"Admin is the password, and you typed {self.username_entry_var.get()}")
			self.notification_message.configure(text="Please continue...", foreground="green")
			self.username_text.configure(foreground="green")

			if self.password_entry_var.get() == "admin":
				"""Correct username and password"""
				print(f"Correct password! {self.password_entry_var.get()}")
				self.destroy_sequence()
			
			elif self.password_entry_var.get() == '':
				"""Correct username, empty password field"""
				print(f"Empty password field not allowed!")
				self.notification_message.configure(text="Input password!", foreground="orange")
				self.password_text.configure(foreground="orange")
			else:
				"""Correct username, wrong password"""
				print("Wrong password, you entered-->", self.password_entry_var.get())
				self.notification_message.configure(text="Wrong password!", foreground="red")
				self.password_text.configure(foreground='red')

		elif self.username_entry_var.get() == '':
			"""Empty username"""
			print("Empty Username!", self.username_entry_var.get())
			self.notification_message.configure(text="Enter Username", foreground='orange')
			self.username_text.configure(foreground='orange')
		
		else:
			"""Invalid username"""
			print(f"Invalid Username, you entered--> {self.username_entry_var.get()}")
			self.notification_message.configure(text='Invalid username!', foreground='red')
			self.username_text.configure(foreground="red")
	
	def destroy_sequence(self) -> None:
		time.sleep(0.8)
		timer : int | float = 100
		contrast : float | int = 1.0
		while timer != 0:
			self.attributes('-alpha', contrast)
			contrast -= 0.01
			timer -= 1
			time.sleep(0.03)
		self.destroy()
	
	def forgot_password_messagebox(self) -> None:
		showinfo(title='Developer help', message="The Correct Username is Admin and the password is admin.\nHappy code testing and don't forget to test the login simulation!")


def center(self):
	"""Ensures the Splashscreen is centered on the Screen"""
	s_width: int = self.winfo_screenwidth()
	s_height: int = self.winfo_screenheight()
	center_x: int = int(s_width / 2 - WIDTH / 2)
	center_y: int = int(s_height / 2 - HEIGHT / 2)
	return self.geometry(f'{WIDTH}x{HEIGHT}+{center_x}+{center_y}')


COLORS: dict[str, str] = {'Dark blue': '#231651', 'Light blue': '#5b5bff', 'Light white': '#dcdcdc', 'Light blue_2': '#476C9B', 'other': '#301a78', 'Grey': '#778899', 'new_2': '#fff000'}
WIDTH : int = 630
HEIGHT : int = 330

if __name__ == '__main__':
	try:
		"""For windows users, this ensures the GUI has sharp pixels and they are not blurry."""
		from ctypes import windll
		windll.shcore.SetProcessDpiAwareness(1)
	except ImportError:
		pass
	
	splashscreen: SplashScreen = SplashScreen()
	splashscreen.mainloop()
	app: Login = Login()
	app.mainloop()