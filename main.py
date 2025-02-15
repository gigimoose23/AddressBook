import tkinter
import tkinter.filedialog
tk = tkinter.Tk()
tk.title("Address Book")
tk.resizable(False, False)
tk.geometry("600x600")

list = tkinter.Listbox(tk)

list.config(width=50,height=16)
list.place(x=30,y=50)
opened = None
def askOpen():
    global opened
    opened = tkinter.filedialog.askopenfile(title="Open Address Book")
    if opened:
        list.insert(0, "ieji")
openBtn = tkinter.Button(tk)
openBtn.config(text="Open", font="Poppins 14", command=askOpen)
openBtn.place(x=400,y=50,anchor="center",height=40,width=80)


tk.mainloop()