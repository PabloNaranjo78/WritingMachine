from tkinter import *


class MainWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("Writing machine IDE")
        self.master.geometry("1000x650+0+0")
        self.master.resizable(False, False)
        self.master.iconbitmap("Images/icon.ico")
        self.master.configure(background="white")
        self.canvas = Canvas(master, width=1000, height=650,highlightthickness=0, relief='ridge')
        self.canvas.place(x=0, y=0)
        self.canvas.configure(bg='#3C3F41')





