import tkinter as tkinter
from tkinter import filedialog
import json
import tkinter.messagebox

tk = tkinter.Tk()
tk.title("Address Book")
tk.resizable(False, False)
tk.geometry("600x500")

listbox = tkinter.Listbox(tk)
listbox.config(width=50, height=16)
listbox.place(x=30, y=50)

opened = None
address_data = {}

def askOpen():
    global opened, address_data
    opened = filedialog.askopenfilename(title="Open Address Book")
    if opened:
        listbox.delete(0, tkinter.END)
        name_var.set("Name")
        phone_var.set("Phone")
        address_var.set("Address")
        birthday_var.set("Birthday")
        with open(opened, "r") as file:
            address_data = json.load(file)
            for name in address_data:
                listbox.insert(tkinter.END, name)
    

def saveData():
    global address_data, opened
    if not opened:
        opened = filedialog.asksaveasfilename(defaultextension=".txt")
    if opened:
        with open(opened, "w") as file:
            json.dump(address_data, file)

def updateData():
    global address_data
    name = name_var.get()
    address = address_var.get()
    phone = phone_var.get()
    birthday = birthday_var.get()
    if name:
        address_data[name] = [address, phone, birthday]
        listbox.insert(tkinter.END, name)

def deletedSelectedData():
    global address_data
    del address_data[name_var.get()]
    try:
        listbox.delete(listbox.curselection())
        name_var.set("Name")
        phone_var.set("Phone")
        address_var.set("Address")
        birthday_var.set("Birthday")
    except:
        tkinter.messagebox.showerror("Error", "Please select something to delete, or use delete all!")

def editData():
    global address_data
    name = name_var.get()
    address = address_var.get()
    phone = phone_var.get()
    birthday = birthday_var.get()
    if name in address_data:
        address_data[name] = [address, phone, birthday]
    else:
        tkinter.messagebox.showerror("Error", "Please select something to edit!")

def deleteAllData():
    global address_data
    address_data = {}
    listbox.delete(0, tkinter.END)

    name_var.set("Name")
    phone_var.set("Phone")
    address_var.set("Address")
    birthday_var.set("Birthday")
    

def fillFields(event):
    selection = listbox.curselection()
    if selection:
        name = listbox.get(selection[0])
        data = address_data.get(name, ["", "", ""])
        name_var.set(name)
        address_var.set(data[0])
        phone_var.set(data[1])
        birthday_var.set(data[2])

listbox.bind("<<ListboxSelect>>", fillFields)

name_var = tkinter.StringVar()
address_var = tkinter.StringVar()
phone_var = tkinter.StringVar()
birthday_var = tkinter.StringVar()

name_entry = tkinter.Entry(tk, textvariable=name_var, font="Poppins 12")
name_entry.place(x=460, y=150, anchor="center", width=200)
name_entry.insert(0, "Name")

address_entry = tkinter.Entry(tk, textvariable=address_var, font="Poppins 12")
address_entry.place(x=460, y=200, anchor="center", width=200)
address_entry.insert(0, "Address")

phone_entry = tkinter.Entry(tk, textvariable=phone_var, font="Poppins 12")
phone_entry.place(x=460, y=250, anchor="center", width=200)
phone_entry.insert(0, "Phone")

birthday_entry = tkinter.Entry(tk, textvariable=birthday_var, font="Poppins 12")
birthday_entry.place(x=460, y=300, anchor="center", width=200)
birthday_entry.insert(0, "Birthday")

openBtn = tkinter.Button(tk, text="Open Address File", font="Poppins 14", command=askOpen)
openBtn.place(x=460, y=50, anchor="center", height=40, width=200)

saveBtn = tkinter.Button(tk, text="Save", font="Poppins 14", command=saveData)
saveBtn.place(x=460, y=400, anchor="center", height=40, width=80)

updateBtn = tkinter.Button(tk, text="Add", font="Poppins 14", command=updateData)
updateBtn.place(x=460, y=350, anchor="center", height=40, width=80)


editBtn = tkinter.Button(tk, text="Edit", font="Poppins 14", command=editData)
editBtn.place(x=370, y=400, anchor="center", height=40, width=80)

deleteBtn = tkinter.Button(tk, text="Delete Selected", font="Poppins 14", command=deletedSelectedData)
deleteBtn.place(x=460, y=450, anchor="center", height=40, width=175)

deleteAllBtn = tkinter.Button(tk, text="Delete All", font="Poppins 14", command=deleteAllData)
deleteAllBtn.place(x=350, y=350, anchor="center", height=40, width=125)

tk.mainloop()
