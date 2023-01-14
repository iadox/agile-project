import tkinter as tk
from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email import utils
from enum import Enum
import sqlite3


obj_list = []
warehouse_obj_list = []
customer_obj_list = []
class Ind:
  def __init__(self,i,w,c):
     self.i = i
     self.w = w 
     self.c = c

  def getI(self):
    return self.i
  def getW(self):
    return self.w
  def getC(self):
    return self.c

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

class Item_attributes():

  def __init__(self, name, location, quantity,price,state):
    self.name = name
    self.location = location
    self.quantity = quantity
    self.price = price
    self.state = state
  
  def getName(self):
    return self.name
  def getLocation(self):
    return self.location
  def getQuantity(self):
    return self.quantity
  def getPrice(self):
    return self.price
  def getState(self):
    return self.state
  
  def Desc(self):
    return f"Item Name: {self.name}, Quantity: {self.quantity}, @ {self.location}, Price: {self.price} $, Current State: {self.state} "

def login():
    for widgets in content.winfo_children():
      widgets.destroy()
    #main_text = Label(content, text = "Login Menu", background='#3d403d',fg='white', font = ("Times New Roman", 20)).pack(fill='x')
    root.geometry('320x125')
    frame = LabelFrame(content, text="  Login to Warehouse System  ", padx=5, pady=5, bg="#77a677")
    frame.pack(padx=10, pady=10)

    # Create the username label and entry
    username_label = Label(frame, text="User Name:", bg="#77a677")
    username_label.grid(row=1, column=0)
    username_entry = Entry(frame, width=15)
    username_entry.grid(row=1, column=1)

    # Create the password label and entry
    password_label = Label(frame, text="Password:", bg="#77a677")
    password_label.grid(row=2, column=0)
    password_entry = Entry(frame, show="*", width=15)
    password_entry.grid(row=2, column=1)
    def set_text(usern, p,v):
        username_entry.delete(0,END)
        username_entry.insert(0, usern)
        password_entry.delete(0,END)
        password_entry.insert(0,p)
        mainmenu(v)
        return
    v = 1
    # Once login button is clicked we come here
    def login_click():
        status = False
        username = username_entry.get()
        password = password_entry.get()
        v=1
        if username == "Admin" and password == "123":
          status = True
          v = 0
        elif username == "Officer" and password == "123":
          status = True
          v = 0
        elif username == "Employee" and password == "123":
          status =True
          v = 1
        verifyLogin(v,status,username_entry,password_entry)
        
    login_button = HoverButton(frame, text="Login",bg="#77a677", command=lambda:login_click())
    login_button.grid(row=4, column=1)
    b1 = HoverButton(frame,text="Test Login as Officer",bg="#77a677",command=lambda:set_text("Officer","123",0))
    b1.grid(row=4, column=2)

def verifyLogin(v,status,username_entry,password_entry):
  if status == True:
    mainmenu(v)
  else:
    messagebox.showerror("Login Failed", "Logged failed, try again")
    username_entry.delete(0, END)
    username_entry.insert(0, "")
    password_entry.delete(0, END)
    password_entry.insert(0, "")
    
def mainmenu(v):
    selected_items=[]
    for widgets in content.winfo_children():
      widgets.destroy()
    root.geometry('550x450')
    main_text = Label(content, text = "Main Menu", background='#3d403d',fg='white', font = ("Times New Roman", 20)).pack(fill='x')
    
    customer_btn = HoverButton(content , text= 'Customer merchandise' ,activebackground='#11aebf', bg='#11fad3' ,height=2,width=20, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:merchendise(v,1))
    customer_btn.pack(padx= 20, pady=30, side = LEFT, anchor="nw")

    warehouse_btn = HoverButton(content , text= 'Warehouse merchandise' ,bg='#e8db7b',activebackground='#baac41', fg='black' ,height=2,width=20, font=("Times New Roman", 13,'bold') , command= lambda:merchendise(v,0))
    warehouse_btn.pack( padx= 20, pady=30, side = RIGHT, anchor="ne")

    back_btn = HoverButton(content , text= 'Back' ,activebackground='#d2f7d2', bg='#77a677' , fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:login())
    back_btn.place(y=4,x=20)

def merchendise(v,merch):
    root.geometry('750x670')
    for widgets in content.winfo_children():
      widgets.destroy()
    back_btn = HoverButton(content , text= 'Back' ,activebackground='#09fb66', bg='#fb5209' , fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:mainmenu(v))
    back_btn.pack(side= TOP, anchor=NW)
    list_title = ""
    if merch == 0:
      list_title = "Warehouse Merchandise Items:"
    elif merch == 1:
      list_title = "Customer Merchandise Items:"
    list_frame= LabelFrame(content, text=list_title ,background='#77a677',font=("Times New Roman", 16) )
    list_frame.pack(pady=20)
    items_list = Listbox(list_frame, width=80, height=30, font=("Arial", 12))
    Warehouse_items_list = Listbox(list_frame, width=80, height=30, font=("Arial", 12))
    Customer_items_list = Listbox(list_frame, width=80, height=30, font=("Arial", 12))
    cursor.execute("SELECT * FROM items")
    full_list = (cursor.fetchall())
    obj_list.clear()
    warehouse_obj_list.clear()
    customer_obj_list.clear()
    for item in full_list:
      item = list(item)
      add_from_db(items_list, Customer_items_list, Warehouse_items_list, item)
    if v == 0:
      add_btn = HoverButton(content , text= '+' ,bg = "#09fb3d", activebackground='#fb09db' ,height=1,width=3, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:add_screen(items_list, Customer_items_list, Warehouse_items_list))
      add_btn.place(x=380,y=4)
      remove_btn = HoverButton(content , text= '-' ,bg='#fb091d',activebackground='#baac41', fg='black' ,height=1,width=3, font=("Times New Roman", 13,'bold') , command= lambda:remove_item(items_list,Warehouse_items_list,Customer_items_list, merch))
      remove_btn.place(x=330, y=4)
      upd_btn = HoverButton(content , text= 'Update' ,activebackground='#11aebf', bg='#11fad3' ,height=1,width=6, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:update_item(items_list,Warehouse_items_list,Customer_items_list,merch))
      upd_btn.place(x=250,y=4)
    if merch == 1:
      Customer_items_list.pack(padx=5, pady=5)
    elif merch == 0:
      Warehouse_items_list.pack(padx=5, pady=5)
    inv_btn = HoverButton(content , text= 'Generate Invoice' ,activebackground='#11aebf', bg='#11fad3' ,height=1,width=13, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:generate_invoice(items_list))
    inv_btn.place(x=100,y=4)
    notify_btn = HoverButton(content , text= 'Notify Customer' ,activebackground='#11aebf', bg='#11fad3' ,height=1,width=13, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:notify(items_list,Warehouse_items_list,Customer_items_list,merch))
    notify_btn.place(x=430,y=4)

def add_screen(items_list, c, w):
    window = tk.Tk()
    window.title('Add Item Screen')
    window.geometry('400x400')
    window.config(bg="#e2d4c9")
    item_label = Label(window, text="Item Name:")
    item_label.pack(padx=5, pady=5)
    item_field = Entry(window, width=35, font=("Arial", 16))
    item_field.pack(padx=5, pady=5)
    quantity_label = Label(window, text="Quantity:")
    quantity_label.pack(padx=5, pady=5)
    quantity_field = Entry(window, width=35, font=("Arial", 16))
    quantity_field.pack(padx=5, pady=5)
    price_label = Label(window, text="Price Per Unit:")
    price_label.pack(padx=5, pady=5)
    price_field = Entry(window, width=35, font=("Arial", 16))
    price_field.pack(padx=5, pady=5)
    location_label = Label(window, text="Category:")
    location_label.pack(padx=5, pady=5)
    Var = StringVar(window)
    location_field = OptionMenu(window, Var, "Warehouse Merchandise", "Customer Merchandise")
    location_field.pack(padx=5, pady=5)
    Var.set("Select Marchandise")
    state_label = Label(window, text="State of the item:")
    state_label.pack(padx=5, pady=5)
    state = StringVar(window)
    state_field = OptionMenu(window, state, "Delivered" ,"Shipping","In_Warehouse" )
    state_field.pack(padx=5, pady=5)
    state.set("Select State of the itme")
    item = Item_attributes(name=item_field,quantity=quantity_field, location=Var,price=price_field, state=state)
    add_btn = HoverButton(window , text= 'Add Item' ,activebackground='#11aebf', bg='#11fad3' ,height=1,width=9, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:add_item(item,items_list, w,c,1))
    add_btn.pack(padx=5, pady=5)

def add_item(item,items_list, w, c,operation):
    try:
        name = item.getName().get()
        quantity = item.getQuantity().get()
        location = item.getLocation().get()
        price = item.getPrice().get()
        state = item.getState().get()
    except:
        name = item.getName()
        quantity = item.getQuantity()
        location = item.getLocation()
        price = item.getPrice()
        state = item.getState()
    item_not_there = True
    StrItem = ""
    '''for i in range(len(obj_list)):
      try:
        if obj_list[i] == f"Item Name: {item.getName().get()}, Quantity: {item.getQuantity().get()}, @ {item.getLocation().get()}, Price: {item.getPrice().get()} $, Current State: {item.getState().get()} ":
          item_not_there = False
      except:
        if obj_list[i] == f"Item Name: {item.getName()}, Quantity: {item.getQuantity()}, @ {item.getLocation()}, Price: {item.getPrice()} $, Current State: {item.getState()} ":
          item_not_there = False
    if add_this:'''
    try:
      StrItem = Item_attributes(name=item.getName().get(),quantity=item.getQuantity().get(), location=item.getLocation().get(),price=item.getPrice().get(),state=item.getState().get())
    except:
      StrItem = Item_attributes(name=item.getName(),quantity=item.getQuantity(), location=item.getLocation(),price=item.getPrice(),state=item.getState())
    items_list.insert(tk.END, f"Item Name: {name}, Quantity: {quantity}, @ {location}, Price: {price} $, Current State: {state} ")
    obj_list.append(StrItem)
    if location == "Warehouse Merchandise":
      warehouse_obj_list.append(StrItem)
      w.insert(tk.END, f"Item Name: {name}, Quantity: {quantity}, @ {location}, Price: {price} $, Current State: {state} ")
    elif location == "Customer Merchandise":
      c.insert(tk.END, f"Item Name: {name}, Quantity: {quantity}, @ {location}, Price: {price} $, Current State: {state} ")
      customer_obj_list.append(StrItem)
    
    query = "INSERT OR IGNORE INTO items VALUES ( ? , ? , ? , ? , ? )"
    params = (name, quantity, price, location, state)
    cursor.execute(query, params)
    con.commit()
    for i in range(len(obj_list)):
      print(i)
      print(obj_list[i].getName())

def remove_item(items_list,w,c, merch):
    selected_item = items_list.curselection()
    selected_w = w.curselection()
    selected_c = c.curselection()
    ini = selected_item
    inw = selected_w
    inc = selected_c
    w_m = w.get(0,END)
    c_m = c.get(0,END)
    items_list_m = items_list.get(0,END)
    if merch == 0:
      inw = inw[0]
      val = w_m[inw]
      ini = items_list_m.index(val)
      row_num = warehouse_obj_list[inw]
    elif merch == 1:
      inc = inc[0]
      val = c_m[inc]
      ini = items_list_m.index(val)
      row_num = customer_obj_list[inc]
    name = row_num.getName()
    print(name)
    select_query = "SELECT rowid FROM items WHERE name = ?"
    select_param = (name, )
    cursor.execute(select_query, select_param)
    fetched_rowid = cursor.fetchone()
    print(fetched_rowid)
    select_query = "SELECT name FROM items WHERE rowid = ?"
    select_param = fetched_rowid
    cursor.execute(select_query, select_param)
    name = cursor.fetchone()
    query = "DELETE FROM items WHERE name = ?"
    params = (name)
    cursor.execute(query, params)
    con.commit()
    print(ini)
    print(selected_item)
    print(selected_w)
    print(selected_c)
    if selected_item:
      items_list.delete((ini))
      obj_list.pop(ini)
    if selected_w:
      w.delete(selected_w)
      warehouse_obj_list.pop(inw)
    elif selected_c:
      c.delete(selected_c)
      customer_obj_list.pop(inc)

def add_from_db(items_list, Customer_items_list, Warehouse_items_list, item):
  objitem = Item_attributes(name=item[0],quantity=item[1], location=item[3],price=item[2], state=item[4])
  add_item(objitem, items_list,Warehouse_items_list,Customer_items_list,0)

def update_item(items_list,w,c,current_screen):
    ini = items_list.curselection()
    inw = w.curselection()
    inc = c.curselection()
    w_m = w.get(0,END)
    items_list_m = items_list.get(0,END)
    c_m = c.get(0,END)
    to_be_deleted = 0
    if current_screen == 0:
      to_be_deleted = inw
      inw = inw[0]
      val = w_m[inw]
      ini = items_list_m.index(val)
    elif current_screen == 1:
      to_be_deleted = inc
      inc = inc[0]
      val = c_m[inc]
      ini = items_list_m.index(val)
    index = Ind(i=ini,w=inw,c=inc)
    ind = 1
    if ini > -1:
      ind = ini
      update_screen(items_list, obj_list[ind],w,c,index,items_list_m,w_m,c_m,to_be_deleted)
    elif inw > -1:
      ind = inw
      update_screen(items_list, obj_list[ind],w,c,index,items_list_m,w_m,c_m,to_be_deleted)
    elif inc > -1:
      ind = inc
      update_screen(items_list, obj_list[ind],w,c,index,items_list_m,w_m,c_m,to_be_deleted)

def update_screen(items_list, old,w,c,index,m1,m2,m3,tbd):
    window = tk.Tk()
    window.title('Update Item Screen')
    window.geometry('400x400')
    window.config(bg="#e2d4c9")
    item_label = Label(window, text="Item Name:")
    item_label.pack(padx=5, pady=5)
    item_field = Entry(window, width=35, font=("Arial", 16))
    item_field.insert(END,old.getName())
    item_field.pack(padx=5, pady=5)
    quantity_label = Label(window, text="Quantity:")
    quantity_label.pack(padx=5, pady=5)
    quantity_field = Entry(window, width=35, font=("Arial", 16))
    quantity_field.insert(END, old.getQuantity())
    quantity_field.pack(padx=5, pady=5)
    price_label = Label(window, text="Price Per Unit:")
    price_label.pack(padx=5, pady=5)
    price_field = Entry(window, width=35, font=("Arial", 16))
    price_field.insert(END,old.getPrice())
    price_field.pack(padx=5, pady=5)
    location_label = Label(window, text="Category:")
    location_label.pack(padx=5, pady=5)
    Var = StringVar(window)
    location_field = OptionMenu(window, Var, "Warehouse Merchandise", "Customer Merchandise")
    location_field.pack(padx=5, pady=5)
    Var.set(old.getLocation())
    state_label = Label(window, text= "Status of the item")
    state_label.pack(padx=5, pady=5)
    state = StringVar(window)
    state_field = OptionMenu(window, state, "Delivered" ,"Shipping","In_Warehouse")
    state_field.pack(padx=5, pady=5)
    state.set(old.getState())
    item = Item_attributes(name=item_field,quantity=quantity_field, location=Var,price=price_field,state=state)
    add_btn = HoverButton(window , text= 'Update Item' ,activebackground='#11aebf', bg='#11fad3' ,height=1,width=9, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:update_func(items_list, old, item,w,c,index,m1,m2,m3,tbd))
    add_btn.pack(padx=5, pady=5)

def remove_item_up(items_list, old,w,c,index,m1,m2,m3,tbd):
    ini = index.getI() 
    inw = index.getW()
    inc = index.getC()
    inw = (inw,)
    ini = (ini,)
    inc = (inc,)
    m1 = list(m1)
    m2 = list(m2)
    m3 = list(m3)
    if old.getLocation() == "Warehouse Merchandise":
      tbd = inw[0]
      tbd = m2[tbd]
      obj_index = inw[0]
      row_num = warehouse_obj_list[obj_index]
    elif old.getLocation() == "Customer Merchandise":
      tbd = inc[0]
      tbd = m3[tbd]
      obj_index = inc[0]
      row_num = customer_obj_list[obj_index]
    if tbd in m1:
      items_list.delete(ini)
      obj_list.pop(ini[0])
    if tbd in m2:
      w.delete(inw)
      warehouse_obj_list.pop(inw[0])
    elif tbd in m3:
      c.delete(inc)
      customer_obj_list.pop(inc[0])
    name = row_num.getName()
    select_query = "SELECT rowid FROM items WHERE name = ?"
    select_param = (name, )
    cursor.execute(select_query, select_param)
    fetched_rowid = cursor.fetchone()
    select_query = "SELECT name FROM items WHERE rowid = ?"
    select_param = fetched_rowid
    cursor.execute(select_query, select_param)
    name = cursor.fetchone()
    query = "DELETE FROM items WHERE name = ?"
    params = (name)
    cursor.execute(query, params)
    con.commit()

def update_func(items_list, old, item,w,c,index,m1,m2,m3,tbd):
    remove_item_up(items_list, old,w,c,index,m1,m2,m3,tbd)
    add_item(item,items_list,w,c,1)

def generate_invoice(items):
    window = tk.Tk()
    window.title('Item invoice')
    window.geometry('400x400')
    window.config(bg="#e2d4c9")
    label1= Label(window, text='Item Invoice :' ,background='#e2d4c9',font=("Times New Roman", 20) )
    label1.pack()
    text_box = Text(window,font=("Times New Roman", 12), height=15, width=35)
    text_box.pack()
    txt = ""
    for i in range(items.size()):
      text_box.insert(INSERT, f"{items.get(i)} "+"\n")
    ok_btn = HoverButton(window , text= 'Print invoice File' ,activebackground='#d2f7d2', bg='#77a677' , fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:generate_file(window,text_box.get("1.0", "end-1c")))
    ok_btn.pack()

def generate_file(window,text):
  window.destroy()
  with open("Invoice.txt", "w") as f:
        f.write("This an Invoice generated by The WMS:\n")
        f.write(text)

def notify(i,w,c,current_screen):
    ini = i.curselection()
    inw = w.curselection()
    inc = c.curselection()
    w_m = w.get(0,END)
    items_list_m = i.get(0,END)
    c_m = c.get(0,END)
    to_be_emailed = 0
    if current_screen == 0:
      to_be_emailed = inw
      inw = inw[0]
      val = w_m[inw]
      ini = items_list_m.index(val)
    elif current_screen == 1:
      to_be_emailed = inc
      inc = inc[0]
      val = c_m[inc]
      ini = items_list_m.index(val)
    index = Ind(i=ini,w=inw,c=inc)
    ind = ini
    ind = 1
    if ini > -1:
      ind = ini
      notify_screen(obj_list[ind])
    elif inw > -1:
      ind = inw
      notify_screen(obj_list[ind])
    elif inc > -1:
      ind = inc
      notify_screen(obj_list[ind])

def notify_screen(lis):
    window = tk.Tk()
    window.title('Update Item Screen')
    window.geometry('400x400')
    window.config(bg="#e2d4c9")
    name_of_user = Label(window, text="Enter the name of the Customer you want to notify:")
    name_of_user.pack(padx=5, pady=5)
    enter_name = Entry(window, width=35, font=("Arial", 16))
    enter_name.pack(padx=5, pady=5)
    email_of_user = Label(window, text="Please Enter a legit email of the Customer you want to notify:")
    email_of_user.pack(padx=5, pady=5)
    enter_email = Entry(window, width=35, font=("Arial", 16))
    enter_email.pack(padx=5, pady=5)
    send_btn = HoverButton(window , text= 'Notify Customer' ,activebackground='#11aebf', bg='#11fad3' ,height=1,width=12, fg='black' , font=("Times New Roman", 13 ,'bold') ,  command= lambda:send_func(lis,enter_name,enter_email))
    send_btn.pack(padx=5, pady=5)

def send_func(lis,n,em):
    item = "item"
    has = "has"
    itis = "it is"
    is_ = "is"
    sender = 'warehouse.system.deliveries@outlook.com'
    name = n.get()
    customer_email = em.get()
    item_name = lis.getName()
    item_status = lis.getState()
    quantity = float(lis.getQuantity())
    price = float(lis.getPrice())
    if quantity == 1:
      pass
    else:
      item = "items"
      has = "have"
      itis = "they're"
      is_ = "are"
    if item_status == "In_Warehouse":
      item_status = "In our Warehouse"
    elif item_status == "Shipping":
      item_status = "in the process of shipment"
    body = f'''Subject: Your Item has been delivered\n \n\nDear {name},\n\nThe {item} you ordered ({item_name}: Quantity:{quantity}, Total price: {quantity*price}$) {has} been delivered, please pick them up as soon as possible to prevent theft and make sure to set your delivery item status as Recieved.
    \nKind regards, \nThe warehouse'''
    body2 = f'''Subject: Status Update for your Item\n \n\nDear {name},\n\nThe {item} you ordered ({item_name}: Quantity:{quantity}, Total price: {quantity*price}$) {is_} currently {item_status}, Thank you for your patience, we will email you as soon as {itis} delivered to you.
    \nKind regards, \nThe warehouse'''
    body3 = f'''Subject: Status Update for your Item\n \n\nDear {name},\n\nThe {item} you ordered ({item_name}: Quantity:{quantity}, Total price: {quantity*price}$) {is_} currently {item_status}, Thank you for your patience, we will email you as soon as {itis} out for delivery.
    \nKind regards, \nThe warehouse'''
    
    if item_status == "in the process of shipment":
      body = body2
    elif item_status == "In our Warehouse":
      body = body3
    
    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    except Exception as e:
        print(e)
        smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
    type(smtpObj) 
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, "t3mpp@ss") 
    smtpObj.sendmail(sender, customer_email, body) 
    smtpObj.quit()




con = sqlite3.connect('WMS_db.db')
cursor = con.cursor()
command_1 = '''CREATE TABLE IF NOT EXISTS 
items(name TEXT PRIMARY KEY , quantity INTEGER, price FLOAT, location BLOB, status BLOB)'''
cursor.execute(command_1)
root = tk.Tk()
root.title('Warehouse Management System')
root.geometry('635x670')
root.resizable(True,True)
p1 = PhotoImage(file = 'logo.png')
root.iconphoto(False, p1)
content = Frame(root)
content.config(bg="#77a677")
content.pack(fill = BOTH, expand = True)
login()

root.mainloop()