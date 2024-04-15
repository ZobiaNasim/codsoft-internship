from tkinter import*
from random import randint
def pw_gen():
    entry2.delete(0,END)
    pw_len=int(entry1.get())
    passw=""
    for x in range(pw_len):
        passw+=chr(randint(33,126))
    entry2.insert(0,passw)    
pass_gen=Tk()
pass_gen.geometry("600x500")
pass_gen.maxsize(600,500)
pass_gen.minsize(600,500)
pass_gen.title("PASSWORD GENRATOR")
bg=PhotoImage(file="passsword.png")
pic_label=Label(pass_gen,image=bg)
pic_label.place(x=0,y=0,relwidth=1,relheight=1)
password=chr(randint(33,126)) #generate asc characters
label=Label(pass_gen,text="How many characters of password you want?",font=("Helvetica",14),bg="light grey")
label.place(relx=0.04,rely=0.4)
entry1=Entry(pass_gen,font=("Helvetica",14),bg="black",fg="#088F8F")
entry1.place(relx=0.08,rely=0.5)
entry2=Entry(pass_gen,font=("Helvetica",14),bg="black",fg="#088F8F")
entry2.place(relx=0.08,rely=0.6)
frame = Frame(pass_gen, borderwidth=6, bg="black", relief=SUNKEN)
frame.place(relx=0.4, rely=0.8)
b1 = Button(frame, fg="#088F8F", bg="black", text="GENERATE PASSWORD",command=pw_gen)
b1.grid(row=2, column=0)
pass_gen.mainloop()