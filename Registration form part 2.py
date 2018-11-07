from tkinter import *
import sqlite3
import time

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

time1 = ''
clock = Label(root, font=('times', 20, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)
def tick():
    global time1
    clock.place(x=380,y=0)

    time2 = time.strftime('%H:%M:%S')
  
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
 
    clock.after(200, tick)
tick()

Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
   conn.commit()
   
   
             
label_0 = Label(root, text="Student Registration Form",bg='lightgreen',font=("bold", 20))
label_0.place(x=90,y=50)


label_1 = Label(root, text="FullName",bg='lightgreen',font=("bold", 10))
label_1.place(x=70,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="EmailID",bg='lightgreen',font=("bold", 10))
label_2.place(x=70,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",bg='lightgreen',font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male", variable=var, value=1).place(x=240,y=230)
Radiobutton(root, text="Female", variable=var, value=2).place(x=300,y=230)

label_4 = Label(root, text="Country",bg='lightgreen',font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','U.S.A.'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=14)
c.set('Country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming",bg='lightgreen',font=("bold", 10))
label_4.place(x=70,y=330)
var2= IntVar()
Checkbutton(root, text="Java", variable=var1).place(x=240,y=330)

Checkbutton(root, text="Python", variable=var2).place(x=300,y=330)

Button(root, text='Submit',width=20,bg='blue',fg='white',command=database).place(x=180,y=400)

root.config(background="skyblue")
root.mainloop()























