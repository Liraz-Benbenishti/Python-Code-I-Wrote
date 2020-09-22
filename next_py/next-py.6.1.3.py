import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.pinklabel = tk.Label(self.master, 
									text="what's my favorite video?", 
									fg="pink", 
									font="Helvetuca 16 bold")
		self.pinklabel.pack()

		self.button = tk.Button(self.master,
								text="click to find out!",
								command=self.say_hi)
		self.button.pack()

	def say_hi(self):
		frame = tk.Frame(self.master)
		frame.pack()
		self.bar = tk.Frame(root, relief=tk.RIDGE)
		self.bar.pack(side=tk.TOP)
		self.iconPath = 'nextpy.png'
		self.icon = ImageTk.PhotoImage(Image.open(self.iconPath))
		self.image = tk.Label(self.bar)
		self.image.image = self.icon
		self.image.configure(image=self.icon)
		self.image.pack(side=tk.LEFT)

		#image = Image.open("2.jpg")
		#photo = ImageTk.PhotoImage(image)
		#self.image = tk.Label(self.master,
		#							text = "d",
		#							image = photo)
		#self.image.pack(side = "bottom", fill = "both", expand = "yes")

		#self.image.pack()

root = tk.Tk()
app = Application(master=root)

w = tk.Label(root, text="Hello Tkinter!", fg="pink")

try:
	app.mainloop()
except KeyboardInterrupt:
	pass