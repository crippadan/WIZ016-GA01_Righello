import pandas as pd

from tkinter import *

# everything is a widget in tkinter

# main widget
root = Tk()

# create widget
# LabelWidget1 = Label(root, text='Test')
# LabelWidget2 = Label(root, text='N.1')

# add to the screen window in the center and below
# LabelWidget1.pack()
# LabelWidget2.pack()

# add to the screen window in customized position
# LabelWidget1.grid(row=0,column=0)
# LabelWidget2.grid(row=1,column=0)

Question = Label(root, text='Come ti chiami?')
Question.grid(row=0,column=0)

# entry widget
EntryWidget1 = Entry(root, 
                     width=50,
                     borderwidth=5,
                     fg='white',
                     bg='black')
# EntryWidget1.pack()
EntryWidget1.grid(row=0,column=1)
# EntryWidget1.insert(0, 'Come ti chiami? ')  # con questo, il get prende anche la domanda
# EntryWidget1.delete(0,END)                  # cancella tutta l'entry

# button widget
# def myClick(name):
def myClick():
    name = EntryWidget1.get()
    try:
        Label1.delete()
    except:
        pass
    Label1 = Label(root, text=f'Ciao {name}.')
    # Label1.pack()
    Label1.grid(row=1,column=1)

ButtonWidget1 = Button(root, 
                       text='Ok', 
                       state=ACTIVE,        # button is active
                       padx=50, pady=30,    # button size
                    #    command=lambda: myClick('myinput'),     # what happens when button is used
                       command=myClick,    
                       fg='white',          # foreground (text) color
                       bg='black',          # background color
                       )
# ButtonWidget1.pack()
ButtonWidget1.grid(row=0,column=2)

# activate and update screen window
root.mainloop()

