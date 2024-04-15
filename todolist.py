from tkinter import *
todolist = Tk()
tasklist=[]
#functions
def taskfile():
    try:
        global todo
        with open ("todo.txt","r") as todo:
         task=todo.readlines()
        for i in task:
         if i!="\n" :
            tasklist.append(i) 
            list.insert(END,i)
    except:
       file=open("todo.txt","w")  
       file.close()              
def add():
    task=taskentry.get()
    taskentry.delete(0,END)
    if task:
       with open("todo.txt","w") as f:
        f.write(f"\n{task}")
        tasklist.append(task)
        list.insert(0,task)
        f.close()
def Delete() :
   global tasklist
   task=str(list.get(ANCHOR))
   if task in tasklist:
      tasklist.remove(task)   
      with open("todo.txt","w") as file:
         for task in tasklist:
            file.write(task+"\n")
      list.delete(ANCHOR) 
      file.close()     


#main code starts
todolist.geometry("1000x1000")
todolist.minsize(500, 200)
todolist.maxsize(2000, 1000)
todolist.configure(bg="#ADE8F4")
todolist.title("TO DO LIST")
photo = PhotoImage(file="icon.png")
todolist.iconphoto(False, photo)
title = Label(text="TO DO LIST", font=("comicsansms", 20, "bold"), bg="light pink", fg="white", relief=SUNKEN, padx=30, pady=10)
title.place(relx=0.5, rely=0.1, anchor="center")
frame1 = Frame(todolist, borderwidth=6, bg="#ADE8F4", relief=SUNKEN)
frame1.place(relx=0.5, rely=0.55, anchor="center")
frame2 = Frame(todolist, borderwidth=6, bg="#ADE8F4", relief=SUNKEN)
frame2.place(relx=0.5, rely=0.6, anchor="center")
b1 = Button(frame1, fg="white", bg="red", text="ADD",command=add)#button to add
b2 = Button(frame2, fg="white", bg="red", text="DELETE",command=Delete) #button to delete
b1.pack() 
b2.pack()
frame3=Frame(todolist,width=400,height=40,bg="light pink") #entry box to enter task
frame3.place(x=300,y=180)
task1=StringVar()
taskentry=Entry(frame3,width=100,relief=SUNKEN,bg="white",font=('arial',14))
taskentry.place(x=10,y=7)
#task list
frame4=Frame(todolist,bd=3,width=500,height=100,bg="white")
frame4.place(x=280,y=240)
list=Listbox(frame4,font=('arial',14),width=40,height=12,bg="white",cursor="hand2",selectbackground="#5a95ff")
list.pack(side=LEFT,fill=BOTH,padx=2)
#scroll bar
scrollbar=Scrollbar(frame4)
scrollbar.pack(side=RIGHT,fill=BOTH)
list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list.yview)
taskfile()
todolist.mainloop()