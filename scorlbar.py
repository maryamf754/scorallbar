from tkinter import *
win=Tk()
win.geometry("400x500")
win.config(bg="#b8b7b7")
sr=Scrollbar(win)
sr.pack(side='left',fill=Y)
lst=Listbox(win,yscrollcommand=sr.set)
for i in range(50):
    lst.insert(END,"iteam ta 1")
lst.pack(side="left",fill=Y)
sr.config(command=lst.yview)


win.mainloop()