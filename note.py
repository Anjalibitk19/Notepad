from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#function for new file
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

#function for open
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

#save function
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

#exit function
def exitfile():
    root.destroy()

#cut function
def cut():
    TextArea.event_generate(("<>"))

#copy function
def copy():
    TextArea.event_generate(("<>"))

#paste function
def paste():
    TextArea.event_generate(("<>"))



if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Anjali's Notepad")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root)
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # creating menubar
    MenuBar = Menu(root)

    #file menu
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command = openFile)
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = exitfile)
    MenuBar.add_cascade(label = "File", menu=FileMenu)

    # Edit Menu 
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    root.config(menu=MenuBar)

    #Adding Scrollbar 
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    #running mainloop
    root.mainloop()
