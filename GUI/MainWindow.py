from tkinter import *
from tkinter import filedialog


class MainWindow:

    def __init__(self, master):
        self.file_name = ""
        self.master = master
        self.master.title("Writing machine IDE")
        self.master.geometry("1000x650+0+0")
        self.master.resizable(False, False)
        self.master.iconbitmap("Images/icon.ico")
        self.master.configure(background="white")
        self.canvas = Canvas(master, width=1000, height=650,highlightthickness=0, relief='ridge')
        self.canvas.place(x=0, y=0)
        self.canvas.configure(bg='#3C3F41')

        self.menu_bar = Menu(self.master,background='blue', fg='white')
        self.file_menu = Menu(self.menu_bar)
        self.file_menu.add_command(label="Open...", command=self.openFileMenu)
        self.file_menu.add_command(label="Save", command=self.saveFile)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.master.config(menu=self.menu_bar)

        self.editor_text_Scrollbar = Scrollbar(self.canvas)

        self.editor_text = Text(self.canvas, width=90, height=20, font=('Lucida Sans Typewriter', 12),
                                yscrollcommand=self.editor_text_Scrollbar.set)

        self.editor_text.config(bg='#2B2B2B', fg='white')
        self.editor_text_Scrollbar.config(bg='#2B2B2B')

        self.editor_text_Scrollbar.config(command=self.editor_text.yview)
        self.editor_text.place(x=40, y=20)
        self.editor_text_Scrollbar.place(x=950, y=20, height=363)




    def openFileMenu(self):
        self.file_name = filedialog.askopenfilename(initialdir="/", title="Select file")
        self.master.title("Writing machine IDE - " + self.file_name)
        self.editor_text.insert(END, self.file_name)
        print(self.file_name)

    def saveFile(self):
        print("guardar")
