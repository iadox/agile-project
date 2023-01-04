import tkinter as tk
from tkinter import *
class HoverButton(tk.Button):#Use this instead of tk.Button() so the buttons so that when you hover over a button it changes color. -Aburrobb
    def _init_(self, master, **kw):
        tk.Button._init_(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


def generate_invoice(items):
    window = tk.Tk()
    window.title('Item invoice')
    window.geometry('300x300')
    window.config(bg="#e2d4c9")

    label1= Label(window, text='Item Invoice :' ,background='#e2d4c9',font=("Times New Roman", 20) )
    label1.pack()
    text_box = Text(window,font=("Times New Roman", 12), height=10, width=30)
    text_box.pack()
    for i in items:
      text_box.insert(INSERT, i+"\n")
    ok_btn = HoverButton(window , text= 'Ok' ,activebackground='#d2f7d2', bg='#77a677' , fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:window.destroy())
    ok_btn.pack()


def add_item():
  pass

def remove_item():
  pass




def mainmenu(v):
    selected_items=[]
    for widgets in content.winfo_children():
      widgets.destroy()
    main_text = Label(content, text = "Main Menu", background='#3d403d',fg='white', font = ("Times New Roman", 20)).pack(fill='x')
    
    customer_btn = HoverButton(content , text= 'Customer merchandise' ,activebackground='#11aebf', bg='#11fad3' ,height=2,width=20, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:customer_mer(v))
    customer_btn.pack(padx= 20, pady=30, side = LEFT, anchor="nw")

    warehouse_btn = HoverButton(content , text= 'Warehouse merchandise' ,bg='#e8db7b',activebackground='#baac41', fg='black' ,height=2,width=20, font=("Times New Roman", 13,'bold') , command= lambda:warehouse_mer(v))
    warehouse_btn.pack( padx= 20, pady=30, side = RIGHT, anchor="ne")

    back_btn = HoverButton(content , text= 'Back' ,activebackground='#d2f7d2', bg='#77a677' , fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:chooseview())
    back_btn.place(y=4,x=20)

    


def chooseview():
    for widgets in content.winfo_children():
      widgets.destroy()
    main_text = Label(content, text = "Login Menu", background='#3d403d',fg='white', font = ("Times New Roman", 20)).pack(fill='x')
    
    customer_btn = HoverButton(content , text= 'Warehouse Officer or Admin view' ,activebackground='#11aebf', bg='#11fad3' ,height=4,width=30, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:mainmenu(1))
    customer_btn.pack(side= TOP,expand=1)

    warehouse_btn = HoverButton(content , text= 'Employee view' ,bg='#e8db7b',activebackground='#baac41', fg='black' ,height=4,width=30, font=("Times New Roman", 13,'bold') , command= lambda:mainmenu(0))
    warehouse_btn.pack(side=BOTTOM,expand=1)



def customer_mer(v):
    for widgets in content.winfo_children():
      widgets.destroy()
    
    back_btn = HoverButton(content , text= 'Back' ,activebackground='#d2f7d2', bg='#77a677' , fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:mainmenu(v))
    back_btn.pack(side=TOP, anchor=NW)
    label1= Label(content, text='Current items :' ,background='#77a677',font=("Times New Roman", 20) )
    label1.pack()
    customer_items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
    selected_items=[]
    for x in range(len(customer_items)):
      l = Checkbutton(content, text=customer_items[x], variable=customer_items[x],command=lambda x=customer_items[x]:selected_items.append(x))
      l.pack(anchor = CENTER)

    if v == 1:
      add_btn = HoverButton(content , text= '+' ,activebackground='#11aebf', bg='#11fad3' ,height=1,width=3, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:add_item())
      add_btn.place(x=450,y=4)
      remove_btn = HoverButton(content , text= '-' ,bg='#e8db7b',activebackground='#baac41', fg='black' ,height=1,width=3, font=("Times New Roman", 13,'bold') , command= lambda:remove_item())
      remove_btn.place(x=400, y=4)
    inv_btn = HoverButton(content , text= 'Generate Invoice' ,activebackground='#11aebf', bg='#11fad3' ,height=1,width=15, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:generate_invoice(selected_items))
    inv_btn.place(x=100,y=4)


def warehouse_mer(v):
    for widgets in content.winfo_children():
      widgets.destroy()
    back_btn = HoverButton(content , text= 'Back' ,activebackground='#d2f7d2', bg='#77a677' , fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:mainmenu(v))
    back_btn.pack(side= TOP, anchor=NW)
    label2= Label(content, text='Current items :' ,background='#77a677',font=("Times New Roman", 20) )
    label2.pack()
    warehouse_items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
    selected_items=[]
    for x in range(len(warehouse_items)):
      j = Checkbutton(content, text=warehouse_items[x], variable=warehouse_items[x], command=lambda x=warehouse_items[x]:selected_items.append(x))
      j.pack(anchor = CENTER)

    if v == 1:
      add_btn = HoverButton(content , text= '+' ,activebackground='#11aebf', bg='#11fad3' ,height=1,width=3, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:add_item())
      add_btn.place(x=450,y=4)
      remove_btn = HoverButton(content , text= '-' ,bg='#e8db7b',activebackground='#baac41', fg='black' ,height=1,width=3, font=("Times New Roman", 13,'bold') , command= lambda:remove_item())
      remove_btn.place(x=400, y=4)
    inv_btn = HoverButton(content , text= 'Generate Invoice' ,activebackground='#11aebf', bg='#11fad3' ,height=1,width=15, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:generate_invoice(selected_items))
    inv_btn.place(x=100,y=4)


root = tk.Tk()
root.title('Warehouse Management System')
root.geometry('635x610')
root.resizable(False,False)
content = Frame(root)
content.config(bg="#77a677")
content.pack(fill = BOTH, expand = True)
chooseview()




root.mainloop()