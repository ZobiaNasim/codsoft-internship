from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
     if scvalue.get() .isdigit():
        value=int(scvalue.get())
     else:
        try:
           value=eval(scvalue.get()) 
        except Exception as e:
           value="Error"
        scvalue.set(value)
        entry.update()
    elif text =="C":
        scvalue.set("")
        entry.update()
    else:
       scvalue.set(scvalue.get()+text)
       entry.update()        
cal = Tk()
cal.geometry("500x700")
cal.maxsize(500, 700)
cal.minsize(500, 700)
cal.title("CALCULATOR")
photo = PhotoImage(file="cal.png")
cal.iconphoto(False, photo)

frame = Frame(cal, width=550, height=40)
frame.place(x=2, y=20)
scvalue = StringVar()
scvalue.set("")
entry = Entry(frame, textvariable=scvalue, width=550, relief="solid", bg="white", font=('arial', 20))
entry.place(x=2, y=7)

buttons_frame = Frame(cal, bg="grey")
buttons_frame.place(relx=0.05, rely=0.14)
# Creating buttons
for i in range(9, -1, -1):  # Reversed range to start from 9 and go down to 0
    button = Button(buttons_frame, text=str(i), padx=8, pady=10, font="arial 22")
    button.bind("<Button-1>", click)
    button.grid(row=(9 - i) // 3, column=(9 - i) % 3, padx=40, pady=10)
button=Button(buttons_frame,text="-",padx=10, pady=12, font="arial 22") 
button.bind("<Button-1>", click)
button.grid(row=3, column=1, padx=10, pady=10) 
button=Button(buttons_frame,text="/",padx=10, pady=12, font="arial 22") 
button.bind("<Button-1>", click)
button.grid(row=3, column=2, padx=10, pady=10) 
button=Button(buttons_frame,text="+",padx=10, pady=12, font="arial 22") 
button.bind("<Button-1>", click)
button.grid(row=4, column=0, padx=10, pady=10) 
button=Button(buttons_frame,text="x",padx=10, pady=12, font="arial 22") 
button.bind("<Button-1>", click)
button.grid(row=4, column=1, padx=10, pady=10) 
button=Button(buttons_frame,text="=",padx=10, pady=12, font="arial 22") 
button.bind("<Button-1>", click)
button.grid(row=4, column=2, padx=10, pady=10)
button=Button(buttons_frame,text="C",padx=10, pady=12, font="arial 22") 
button.bind("<Button-1>", click)
button.grid(row=5, column=0, padx=10, pady=10)

 
       

cal.mainloop()