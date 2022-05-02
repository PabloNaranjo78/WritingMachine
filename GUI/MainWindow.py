import tkinter
from tkinter import *
from tkinter import filedialog


class MainWindow:

    def __init__(self, master):
        self.file_name = ""
        self.lineCounter = 0
        self.movementScroll = 0.0
        self.master = master
        self.master.title("Writing machine IDE")
        self.master.geometry("1000x650+0+0")
        self.master.resizable(False, False)
        self.master.iconbitmap("Images/icon.ico")
        self.master.configure(background="white")
        self.canvas = Canvas(master, width=1000, height=650, highlightthickness=0, relief='ridge')
        self.canvas.place(x=0, y=0)
        self.canvas.configure(bg='#3C3F41')

        self.menu_bar = Menu(self.master, background='blue', fg='white')
        self.file_menu = Menu(self.menu_bar)
        self.file_menu.add_command(label="Open...", command=self.openFileMenu)
        self.file_menu.add_command(label="Save", command=self.saveFile)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.master.config(menu=self.menu_bar)

        self.editor_text_Scrollbar = Scrollbar(self.canvas)

        self.numberLine = Text(self.canvas, width=4, height=21, bg='#313335', fg="#A2A1A1",
                               font=('Lucida Sans Typewriter', 11),
                               yscrollcommand=self.editor_text_Scrollbar.set)
        self.numberLine.insert(1.0, "1")
        self.numberLine.config(state=DISABLED)
        self.numberLine.place(x=1, y=20)

        self.editor_text = Text(self.canvas, width=104, height=21, font=('Lucida Sans Typewriter', 11),
                                yscrollcommand=self.editor_text_Scrollbar.set)

        self.editor_text.bind("<KeyPress>", self.keyPress)

        self.editor_text.config(bg='#2B2B2B', fg='white')
        self.editor_text_Scrollbar.config(bg='#2B2B2B')

        self.editor_text_Scrollbar.config(command=self.multipleScroll)

        self.editor_text.place(x=40, y=20)
        self.editor_text_Scrollbar.place(x=980, y=20, height=361)

        self.canvas.bind_all("<MouseWheel>", self.scroll)

    def multipleScroll(self, *args):
        self.editor_text.yview(*args)
        self.numberLine.yview(*args)

    def scroll(self, event):
        self.movementScroll = self.editor_text.yview()[0]
        self.numberLine.yview("moveto", self.movementScroll)
        return 'break'

    def openFileMenu(self):
        filetypes = (("Text files", "*.txt"), ("All files", "*.*"))

        self.file_name = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=filetypes)
        self.master.title("Writing machine IDE - " + self.file_name)
        self.editor_text.insert(END, self.file_name)
        self.loadFile(self.file_name)

    def saveFile(self):
        print("guardar")

    def keyPress(self, event):
        self.updateLines()

    def updateLines(self):
        lines = 0
        for i in self.editor_text.get(1.0, END):
            if i == "\n":
                lines += 1
        self.numberLine.config(state=NORMAL)
        self.numberLine.delete(1.0, END)
        for i in range(1, lines + 1):
            if i == 1:
                self.numberLine.insert(END, str(i))
            else:
                self.numberLine.insert(END, "\n" + str(i))
        self.numberLine.config(state=DISABLED)
        self.movementScroll = self.editor_text.yview()[0]
        self.numberLine.yview("moveto", self.movementScroll)

    def loadFile(self, file_name):
        file = open(file_name, "r", encoding="utf-8")
        self.editor_text.delete(1.0, END)
        self.editor_text.insert(END, file.read())
        file.close()
        self.updateLines()
