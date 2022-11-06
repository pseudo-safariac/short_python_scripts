#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk

import threading
import time

class SplashScreen(tk.Tk):
	def __init__(self) -> None:
		super(SplashScreen,self).__init__()
		self.attributes('-topmost', 1)
		self.attributes('-alpha', 0.0)
		self.overrideredirect(True)
		self.config(bg=COLORS['Dark blue'])

		# Visual Fade-in effect
		self.center()
		visual_fade: threading.Thread = threading.Thread(target=self.alpha_settings)
		visual_fade.start()

		# Styling of the widgets
		s: ttk.Style = ttk.Style()
		s.theme_use('clam')
		s.configure('TButton', background = [('focus', COLORS['Dark blue'])], foreground = [('focus', COLORS['Dark blue'])])

		# Styling Company Label Widget
		s.configure('company.TButton', background=COLORS['Dark blue'], foreground= COLORS['New'], font= ('Helvetica', 49, 'bold'), borderwidth= 0, width=11)
		s.map('company.TButton', background=[('active', COLORS['Dark blue'])], foreground=[('active', COLORS['Light white'])])

		# Styling Lab Label Widget
		s.configure('lab.TButton', background= COLORS['Dark blue'],foreground= COLORS['New'], font=('Proxima Nova', 27, 'bold', 'italic'), borderwidth=0, width=4)
		s.map('lab.TButton', background=[('active', COLORS['Dark blue'])],foreground=[('active', COLORS['Light white'])])

		# Styling close Label Widget
		s.configure('close.TButton', background=COLORS['Dark blue'],foreground=COLORS['Light white'], font=('Proxima Nova', 9, 'bold'), borderwidth=0, width=6)
		s.map('close.TButton', background=[('active', COLORS['other'])], foreground=[('active', COLORS['Light white'])])

		# Adding Button Widgets
		company_label: ttk.Button = ttk.Button(self, text = 'WALTER\'S', style= 'company.TButton')
		company_label.place(x=50, y=80)

		lab_label: ttk.Button = ttk.Button(self, text='Lab', style= 'lab.TButton')
		lab_label.place(x=440, y=180)

		close_button : ttk.Button = ttk.Button(self, text='close', style= 'close.TButton', command= self.destroy)
		close_button.place(x=570, y=5)

	def center(self):
		"""Ensures the Splashscreen is centered on the Screen"""
		s_width: int = self.winfo_screenwidth()
		s_height: int = self.winfo_screenheight()
		center_x: int = int(s_width / 2 - WIDTH / 2)
		center_y: int = int(s_height / 2 - HEIGHT / 2)
		return self.geometry(f'{WIDTH}x{HEIGHT}+{center_x}+{center_y}')

	def alpha_settings(self) -> None:
		"""The function gradually changes the contrast of the tkinter application."""
		timer : int | float = 500
		contrast : float | int = 0.5
		while timer != 0:
			self.attributes('-alpha', contrast)
			contrast += 0.01
			timer -= 1
			time.sleep(0.03)


class Login(tk.Tk):
	def __init__(self) -> None:
		super(Login, self).__init__()
		# self.wm_iconbitmap(default="path/pic_1.ico")
		self.wm_title('Splash Login')
		self.attributes('-topmost', 1)
		self.attributes('-alpha', 0.99)
		self.wm_overrideredirect(True)
		self.config(bg=COLORS['Dark blue'])



COLORS: dict[str, str] = {'Dark blue': '#231651', 'Light blue': '#5b5bff', 'Light white': '#dcdcdc', 'New': '#476C9B', 'other': '#301a78'}
WIDTH : int = 630
HEIGHT : int = 330

if __name__ == '__main__':
	try:
		"""For windows users, this ensures the GUI has sharp pixels and they are not blurry."""
		from ctypes import windll
		windll.shcore.SetProcessDpiAwareness(1)
		app: Login = Login()
		app.mainloop()
	except tk.TclError as e:
		print(f"A tkinter error has been raised:\n{e}")
	