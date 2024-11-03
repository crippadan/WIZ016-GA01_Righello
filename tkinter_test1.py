from tkinter import *
from PIL import ImageTk, Image # needed because tkinter doesn't support standard pictures like jpg

def myClick():
    name = EntryWidget1.get()
    Label1 = Label(root, text=f'Ciao {name}.')
    Label1.grid(row=2,column=1)
    try:
        ImageWidget1.destroy()
    except:
        pass

icon_path = r'download-icon-cat-131994967688089922_16.ico'

root = Tk()
root.title('Ruler')
root.iconbitmap(icon_path) # da usare poi per aggiungere il mio logo

quit_button = Button(root, text='Exit', command=root.quit)
quit_button.grid(row=0,column=1)

Question = Label(root, text='Come ti chiami?')
Question.grid(row=1,column=0)

EntryWidget1 = Entry(root, 
                     width=50,
                     borderwidth=5)

EntryWidget1.grid(row=1,column=1)

ButtonWidget1 = Button(root, 
                       text='Ok',
                       command=myClick,
                       padx=30
                       )
ButtonWidget1.grid(row=1,column=2)

img_path = r'pngtree-isolated-cat-on-white-background-png-image_7094927.png'
my_img = ImageTk.PhotoImage(Image.open(img_path))
ImageWidget1 = Label(image=my_img)
ImageWidget1.grid(row=3,column=1)

root.mainloop()