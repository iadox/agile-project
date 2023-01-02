import tkinter as tk
from tkinter import *


def mainmenu():
    for widgets in content.winfo_children():
      widgets.destroy()
    main_text = Label(content, text = "Welcome to WMS ", background='#e2d4c9', font = ("Times New Roman", 20)).place(x=115 , y=0)

    customer_btn = Button(content , text= 'Customer merchandise' , bg='#232325' , fg='#eeeef0' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:customer_mer())
    customer_btn.pack(side= LEFT)

    warehouse_btn = Button(content , text= 'Warehouse merchandise' , bg='#232325', fg='#eeeef0' , font=("Times New Roman", 13,'bold') , command= lambda:warehouse_mer())
    warehouse_btn.pack(side= RIGHT)


def customer_mer():
    for widgets in content.winfo_children():
      widgets.destroy()
    back_btn = Button(content , text= 'go back' , bg='#232325' , fg='#eeeef0' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:mainmenu())
    back_btn.pack(side = LEFT)
    label1= Label(content, text='Current items :' ,background='#e2d4c9',font=("Times New Roman", 20) )
    label1.pack()
    listbox = Listbox(content , selectmode=MULTIPLE)
    listbox.insert(1 , 'Item A')
    listbox.insert(1 , 'Item B')
    listbox.insert(1 , 'Item C')
    listbox.insert(1 , 'Item D')
    listbox.pack()


def warehouse_mer():
    for widgets in content.winfo_children():
      widgets.destroy()
    back_btn = Button(content , text= 'go back' , bg='#232325' , fg='#eeeef0' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:mainmenu())
    back_btn.pack(side = LEFT)
    label2= Label(content, text='Current items :' ,background='#e2d4c9',font=("Times New Roman", 20) )
    label2.pack()
    listbox = Listbox(content , selectmode=MULTIPLE)
    listbox.insert(1 , 'Item E')
    listbox.insert(1 , 'Item F')
    listbox.insert(1 , 'Item G')
    listbox.insert(1 , 'Item H')
    listbox.pack()



root = tk.Tk()
root.title('WMS')
root.geometry('475x200')
content = Frame(root)
content.config(bg="#e2d4c9")
content.pack(fill = BOTH, expand = True)
mainmenu()




root.mainloop()




