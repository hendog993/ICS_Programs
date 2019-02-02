"""
Henry Gilbert
Project: ICS Waitlist Python GUI
Created: 11/29/2018
Updated: 12/8/2018

contributors: Henry Gilbert, etc

Functionality to add:
    - update button to remove prints from list once completed
    - Dropbox file that can holds the queued files and deletes
      them with the update button once completed
    - Make everything look a little better, perhaps us ttk
    - Add a scroll feature to help with longer lists
"""

from tkinter import *
from datetime import datetime

root = Tk()
root.title("ICS 3D Printer Waitlist")
root.geometry('900x400')
count = 0

def queue_button():
    """
    Uses the printobj class to create an object, n, with attributes from
    the tkinter text entries. The first attribute is the file name, the
    second is the printer name, and the third is the time. Per iteration,
    the button creates a row of the objects at the count + 5 row index. Here
    the function creates two checkboxes that show the status of the print;
    """

    global count
    n = PrintObj(fileName.get(0.0, END), printerName.get(0.0, END))
    fileName.delete(0.0, END)
    printerName.delete(0.0, END)
    queuedprintname = Text(root, width=21, height=1)
    queuedprintname.grid(row=count + 5, column=0, sticky="W")
    queuedprintprinter = Text(root, width=17, height=1)
    queuedprintprinter.grid(row=count + 5, column=1, sticky="")
    queuedprintname.insert(0.0, n.name)
    queuedprintprinter.insert(0.0, n.printer)
    Label(root, text=n.timer).grid(row=count + 5, column=1, sticky="E")
    Checkbutton(root, text="In Prog").grid(row=count + 5, column=2, sticky="W")
    Checkbutton(root, text="Complete").grid(row=count + 5, column=3, sticky="W")
    count += 1
    return

"""
    Printer object creator. Serves as a way to only use one object to create
    a unique row in the queued section. The timer is set from the current time
    as a string.
"""

class PrintObj:
    def __init__(self, name, printer, timer=None):
        self.name = name
        self.printer = printer
        time1 = str(datetime.now().time())
        self.timer = time1[0:5]
        return

    pass

"""
Primary Tkinter data holders. Below are the text entries for the
file names, the printer names, and the queue button.
"""
fileLocationLabel = Label(root,
                          text="      FILE NAME: ").grid(row=0, column=0, sticky="W")
fileName = Text(root, width=45, height=1, bg="gray")
fileName.grid(row=0, column=1, sticky="W")

addToQueue = Button(root, width=10, text="QUEUE", command=queue_button)
addToQueue.grid(row=1, column=1, sticky="E")

printerName = Text(root, width=30, height=1, bg="gray")
printerName.grid(row=1, column=1, sticky="w")
printerLabel = Label(root, text="PRINTER").grid(row=1, column=0)

# Label section. Purely aesthetic and serves as column placeholders;

queueLabel = Label(root, text="QUEUED PRINTS",
                   font='Helvetica 18 bold').grid(row=3, columnspan=10)
fileNameLabel = Label(root, text="FILE NAME",
                      font="Helvitica 16 bold").grid(row=4, column=0, sticky="W")
printerNameLabel = Label(root, text="PRINTER",
                         font="Helvitica 16 bold").grid(row=4, column=1, sticky="")
statusLabel = Label(root, text="STATUS",
                    font="Helvitica 16 bold").grid(row=4, column=2, sticky="")
completedLabel = Label(root, text="TIME",
                       font="Helvitica 16 bold").grid(row=4, column=1, sticky="E")
root.mainloop()
